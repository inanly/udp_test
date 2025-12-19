# udp_client.py

# 1. 導入所需函式庫
import socket
import time
import sys     # 導入系統相關功能，用來讀取命令列參數

# --- 設定 ---
# 2. 檢查使用者是否提供了正確的命令列參數
#    sys.argv 是一個列表，包含了使用者執行的指令，例如 ['udp_client.py', '127.0.0.1', '5005']
#    如果列表長度不等於3，代表使用者沒有提供IP和Port，就印出使用說明並結束程式。
if len(sys.argv) != 3:
    print("用法: python udp_client.py <伺服器IP> <連接埠>")
    sys.exit(1)

# 3. 從命令列參數中讀取伺服器的 IP 位址和連接埠
SERVER_IP = sys.argv[1]         # 第一個參數是 IP
SERVER_PORT = int(sys.argv[2])  # 第二個參數是 Port，並將其從字串轉換為整數

# 4. 設定每秒要發送多少個數據包
PACKETS_PER_SECOND = 100
# 5. 計算每個數據包之間的發送間隔時間（秒）
SLEEP_INTERVAL = 1.0 / PACKETS_PER_SECOND

# 6. 建立一個 UDP socket，和伺服器端一樣
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 7. 打印一條訊息，表示客戶端已啟動
print(f"UDP 客戶端啟動，將以每秒 {PACKETS_PER_SECOND} 個封包的速度發送到 {SERVER_IP}:{SERVER_PORT}")

# 8. 使用 try...finally 結構，確保程式結束時能正常關閉
try:
    # 9. 進入一個無限迴圈，讓客戶端可以持續不斷地發送數據
    while True:
        # 10. 獲取當前的高精度時間戳，作為「發送時間」
        timestamp = time.time()
        
        # 11. 將時間戳轉換成位元組 (bytes) 格式的訊息，才能透過網路傳送
        #     - str(timestamp): 將數字時間戳轉換為字串。
        #     - .encode('utf-8'): 將字串編碼成位元組。
        message = str(timestamp).encode('utf-8')
        
        # 12. 將訊息 (message) 發送到指定的伺服器 IP 和 Port
        client_socket.sendto(message, (SERVER_IP, SERVER_PORT))
        
        # 13. 讓程式暫停一小段時間，以精準控制發送頻率
        time.sleep(SLEEP_INTERVAL)

# 14. 當使用者按下 Ctrl+C 時，跳出迴圈
except KeyboardInterrupt:
    print("\n客戶端關閉。")
finally:
    # 15. 無論如何，最後都關閉 socket
    client_socket.close()