#include <stdio.h>

// 插入排序函數
void insertionSort(int a[], int n) {
    int i, j, temp, swapCount = 0;

    // 從第二個元素開始排序
    for (i = 0; i <= n; i++) {
        j = i;

        // 當前元素小於前一個元素時，進行交換
        while (j >= 1 && a[j] < a[j - 1]) {
            // 交換 a[j] 和 a[j-1]
            temp = a[j];
            a[j] = a[j - 1];
            a[j - 1] = temp;

            swapCount++; // 記錄交換次數
            j--;         // 繼續向前比較
        }
    }

    // 輸出排序後的數列
    printf("Sorted array: ");
    for (i = 0; i <= n; i++) {
        printf("%d ", a[i]);
    }
    printf("\nTotal swaps: %d\n", swapCount); // 輸出交換次數
}

int main() {
    // 測試數列 (a[0] 不使用，方便從 1 開始)
    int a[] = {3, 9, 6, 5, 8, 2};
    int n = 6; // 數列長度

    // 執行插入排序
    insertionSort(a, n);

    return 0;
}
