# udp_client.py

import socket
import time
import sys

# --- 設定 ---
if len(sys.argv) != 3:
    # 檢查命令列參數數量，若不正確則顯示用法並結束
    print("用法: python udp_client.py <伺服器IP> <連接埠>")
    sys.exit(1)

SERVER_IP = sys.argv[1]           # 從命令列取得伺服器 IP 位址（sys.argv[1] 是執行程式時輸入的第一個參數）
SERVER_PORT = int(sys.argv[2])    # 從命令列取得伺服器連接埠（sys.argv[2] 是第二個參數，轉成整數型態）
PACKETS_PER_SECOND = 100          # 設定每秒要發送幾個封包（這裡固定為 100）
SLEEP_INTERVAL = 1.0 / PACKETS_PER_SECOND  # 每個封包之間要間隔多久（秒），例如 100 封包/秒就是 0.01 秒/封包

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # 建立UDP socket
print(f"UDP 客戶端啟動，將以每秒 {PACKETS_PER_SECOND} 個封包的速度發送到 {SERVER_IP}:{SERVER_PORT}")

try:
    while True:
        timestamp = time.time()  # 取得目前時間（浮點數，單位為秒）
        message = str(timestamp).encode('utf-8')  # 將時間轉為字串並編碼成位元組
        client_socket.sendto(message, (SERVER_IP, SERVER_PORT))  # 發送封包到伺服器
        time.sleep(SLEEP_INTERVAL)  # 等待一段時間再發送下一個封包
except KeyboardInterrupt:
    # 捕捉 Ctrl+C 中斷，友善結束客戶端
    print("\n客戶端關閉。")
finally:
    # 關閉 socket，釋放資源
    client_socket.close()