# udp_server.py


import socket 
import time    


# --- 設定 ---
# 2. 設置伺服器監聽的主機地址
HOST = '0.0.0.0'  # '0.0.0.0' 是一個特殊地址，表示本地所有IP地址。可以接收來自任何網路介面的資料。


# 3. 設置伺服器監聽的連接埠
PORT = 50005


# 4. 建立網路通訊端點 (socket)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


# 5. 將socket綁定到指定的主機和連接埠
server_socket.bind((HOST, PORT))


# 6. 顯示伺服器已啟動並等待連線
print(f"UDP伺服器已啟動。正在監聽 {HOST}:{PORT}")


# 7. 使用try...finally結構確保在退出時關閉資源
try:
    # 8. 進入無限迴圈，使伺服器能夠持續接收資料
    while True:
        # 9. 等待並接收客戶端資料。這是一個阻塞操作。
        #    - data: 接收到的資料包內容 (bytes)
        #    - addr: 發送方的IP地址和連接埠
        #    - 1024: 本次可接收的最大資料大小（緩衝區大小）
        data, addr = server_socket.recvfrom(1024)
       
        # 10. 記錄資料包接收時的當前時間戳，作為到達時間
        arrival_time = time.time()
       
        # 11. 再次使用try...except來處理無效資料
        try:
            # 12. 將接收到的位元組資料解碼為字串，並轉換為浮點數（發送時間）
            send_time = float(data.decode('utf-8'))
           
            # 13. 核心計算：計算端對端延遲（秒）
            latency_seconds = arrival_time - send_time
           
           
            # 14. 將延遲從秒轉換為毫秒(ms)以便顯示
            latency_ms = latency_seconds * 1000
           
            # 15. 輸出最終的延遲資料。:.3f 表示保留小數點後3位
            print(f"延遲:{latency_ms:.3f}ms")


        except (ValueError, UnicodeDecodeError):
            # 16. 當接收到的資料無法解碼或無法轉換為數值時顯示錯誤訊息
            print("錯誤: 接收到無效資料")


# 17. 當使用者按下Ctrl+C時，KeyboardInterrupt被觸發，退出迴圈
except KeyboardInterrupt:
    print("\n伺服器已終止。")
finally:
    # 18. 無論程式如何結束，最後都要關閉socket以釋放網路資源
    server_socket.close()
