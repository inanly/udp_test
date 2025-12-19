package main

import (
	"context"
	"encoding/json"
	"fmt"
	"log"
	"os"
	"path/filepath"
	"time"

	corev1 "k8s.io/api/core/v1"
	metav1 "k8s.io/apimachinery/pkg/apis/meta/v1"
	"k8s.io/apimachinery/pkg/types"
	"k8s.io/client-go/informers"
	"k8s.io/client-go/kubernetes"
	"k8s.io/client-go/rest"
	"k8s.io/client-go/tools/cache"
	"k8s.io/client-go/tools/clientcmd"
)

func main() {
	// --- 1. 建立連線 (智慧判斷版) ---
	var config *rest.Config
	var err error

	// A. 嘗試讀取本地 KubeConfig (開發模式)
	var kubeconfigPath string
	if homeDir, err := os.UserHomeDir(); err == nil {
		kubeconfigPath = filepath.Join(homeDir, ".kube", "config")
	}

	config, err = clientcmd.BuildConfigFromFlags("", kubeconfigPath)
	if err != nil {
		// B. In-Cluster Config (正式部署模式)
		fmt.Println("[Init] 本地 KubeConfig 讀取失敗，切換至 In-Cluster Config...")
		config, err = rest.InClusterConfig()
		if err != nil {
			log.Fatalf("[Fatal] 無法建立 K8s 連線: %v", err)
		}
		fmt.Println("[Init] >>> In-Cluster Config 連線成功 (Pod 模式)")
	} else {
		fmt.Println("[Init] >>> 本地 KubeConfig 連線成功 (Dev 模式)")
	}

	clientset, err := kubernetes.NewForConfig(config)
	if err != nil {
		log.Fatalf("[Fatal] Clientset 建立失敗: %v", err)
	}

	fmt.Println("--- RT-Controller (v2: QoS Logic) 啟動 ---")

	// --- 2. 設定 Informer ---
	// 監控 default namespace 下的 Pod
	informerFactory := informers.NewSharedInformerFactoryWithOptions(clientset, time.Minute, informers.WithNamespace("default"))
	podInformer := informerFactory.Core().V1().Pods()

	// --- 3. 註冊事件處理器 ---
	podInformer.Informer().AddEventHandler(cache.ResourceEventHandlerFuncs{
		AddFunc: func(obj interface{}) {
			pod := obj.(*corev1.Pod)
			// 新增 Pod 時檢查
			reconcile(clientset, pod)
		},
		UpdateFunc: func(oldObj, newObj interface{}) {
			oldPod := oldObj.(*corev1.Pod)
			newPod := newObj.(*corev1.Pod)

			// 只有當 ResourceVersion 或 Labels 改變時才觸發，避免無限迴圈
			if oldPod.ResourceVersion != newPod.ResourceVersion {
				reconcile(clientset, newPod)
			}
		},
	})

	// --- 4. 啟動迴圈 ---
	stopCh := make(chan struct{})
	defer close(stopCh)
	informerFactory.Start(stopCh)

	fmt.Println("[Status] 等待 Informer 快取同步...")
	if !cache.WaitForCacheSync(stopCh, podInformer.Informer().HasSynced) {
		log.Fatal("[Fatal] 快取同步失敗")
	}

	fmt.Println("[Status] 控制器就緒，開始監控 QoS 與標籤...")
	<-stopCh
}

// --- 核心邏輯：Reconcile (調解) ---
// 整合了 Detect (偵測), QoS Check (檢查), Act (行動)
func reconcile(clientset *kubernetes.Clientset, pod *corev1.Pod) {
	// 1. [Detect] 檢查是否有目標標籤
	if val, ok := pod.Labels["real-time"]; !ok || val != "true" {
		return // 不是目標 Pod，直接忽略
	}

	// 2. [Idempotency] 檢查是否已經處理過
	// 如果已經標記為 processed，且 QoS 狀態也已經紀錄，就跳過
	if pod.Annotations["rt-controller.io/status"] == "processed" {
		return
	}

	fmt.Printf("[Detect] 發現目標 Pod: %s\n", pod.Name)

	// 3. [Logic] QoS 判定 (核心新增功能)
	isGuaranteed, reason := checkQoS(pod)
	qosStatus := "Guaranteed"
	if !isGuaranteed {
		qosStatus = "Not-Guaranteed"
		fmt.Printf("[Warning] Pod %s 設定不符合 Guaranteed QoS! 原因: %s\n", pod.Name, reason)
	} else {
		fmt.Printf("[Info] Pod %s 符合 Guaranteed QoS (準備進行 CPU Pinning)\n", pod.Name)
	}

	// 4. [Act] Patch (寫入結果)
	// 我們將 QoS 的檢查結果也寫入 Annotation，方便除錯
	patchData := map[string]interface{}{
		"metadata": map[string]interface{}{
			"annotations": map[string]string{
				"rt-controller.io/status":     "processed",
				"rt-controller.io/qos-check":  qosStatus,
				"rt-controller.io/qos-reason": reason,
			},
		},
	}

	patchBytes, err := json.Marshal(patchData)
	if err != nil {
		log.Printf("[Error] JSON 序列化失敗: %v", err)
		return
	}

	_, err = clientset.CoreV1().Pods(pod.Namespace).Patch(
		context.TODO(),
		pod.Name,
		types.StrategicMergePatchType,
		patchBytes,
		metav1.PatchOptions{},
	)

	if err != nil {
		log.Printf("[Error] Patch 失敗: %v", err)
	} else {
		fmt.Printf("[Act] 成功更新 Pod %s (Status: processed, QoS: %s)\n", pod.Name, qosStatus)
	}
}

// --- 輔助邏輯：檢查 Pod 是否為 Guaranteed QoS ---
// 規則：所有 Container 的 (CPU Request == CPU Limit) 且 (Memory Request == Memory Limit)
// 且數值不能為 0
func checkQoS(pod *corev1.Pod) (bool, string) {
	for _, container := range pod.Spec.Containers {
		// 1. 檢查 CPU
		reqCPU := container.Resources.Requests.Cpu()
		limCPU := container.Resources.Limits.Cpu()
		
		if reqCPU.IsZero() || limCPU.IsZero() {
			return false, fmt.Sprintf("容器 %s 未設定 CPU Requests 或 Limits", container.Name)
		}
		if !reqCPU.Equal(*limCPU) {
			return false, fmt.Sprintf("容器 %s CPU Requests (%s) != Limits (%s)", container.Name, reqCPU.String(), limCPU.String())
		}

		// 2. 檢查 Memory
		reqMem := container.Resources.Requests.Memory()
		limMem := container.Resources.Limits.Memory()

		if reqMem.IsZero() || limMem.IsZero() {
			return false, fmt.Sprintf("容器 %s 未設定 Memory Requests 或 Limits", container.Name)
		}
		if !reqMem.Equal(*limMem) {
			return false, fmt.Sprintf("容器 %s Memory Requests != Limits", container.Name)
		}
	}
	return true, "OK"
}