# udp_server.py

import socket
import time

# --- 設定 ---
# HOST = '0.0.0.0' 表示監聽所有網路介面（含本機回環、實體網卡等）
# 若只想監聽本機可改為 '127.0.0.1'；若要綁定特定介面則填該介面的 IP
HOST = '0.0.0.0'  # 監聽所有網路介面
PORT = 5005       # 監聽的UDP連接埠（要與 client 發送的埠相同）

# 建立 UDP socket
# socket.AF_INET 表示 IPv4；socket.SOCK_DGRAM 表示 UDP 協定（無連線、不保證到達）
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((HOST, PORT))  # 綁定主機與埠口，之後會被動接收送到此埠的封包

print(f"UDP 伺服器已啟動，正在監聽 {HOST}:{PORT}")

try:
    while True:
        # recvfrom 是阻塞呼叫，直到收到資料才繼續
        # 1024 為一次讀取的最大位元組數 (buffer size)；若封包更大會被截斷
        # 回傳值 data 是 bytes，addr 是 (ip, port) 的 tuple，代表發送者位址
        data, addr = server_socket.recvfrom(1024)
        
        # arrival_time 記錄伺服器收到封包的系統時間（使用 time.time()，單位為秒，浮點）
        # 注意：time.time() 的起點是系統時間，精度與解析度取決於平台與作業系統
        arrival_time = time.time()
        
        try:
            # 預期 client 發送的是一個代表發送時間的字串（例如 "169XXXX.XXXX"）
            # 先將 bytes 解碼成 utf-8 的字串，再轉成 float
            # send_time 是 client 當時呼叫 time.time() 的值（若 client 與 server 時鐘不同，會有偏差）
            send_time = float(data.decode('utf-8'))
            
            # latency_seconds 為從 client 發送時間到 server 收到的差（秒）
            # latency_ms 則是毫秒（ms），常用於顯示網路延遲
            latency_seconds = arrival_time - send_time
            latency_ms = latency_seconds * 1000
            
            # 輸出延遲資訊；格式化到小數點後三位（毫秒精度）
            # 範例輸出： LATENCY:10.123ms
            print(f"LATENCY:{latency_ms:.3f}ms  from {addr}")

            # 注意事項：
            # - 若 client 與 server 時鐘不同 (clock skew)，計算出來的延遲會包含時鐘差異。
            #   若需精確測量應使用同步時鐘（例如 NTP）或採用雙向量測（round-trip）方式。
            # - UDP 是無連線、不保證送達的協定：封包可能遺失、重複或順序錯亂。
            # - 若需要更大吞吐量或頻繁量測，考慮非阻塞或使用 select/epoll/asyncio 來避免單一阻塞影響其他處理。
            
        except (ValueError, UnicodeDecodeError):
            # 若收到的資料不是可以解析成浮點數的時間戳，或編碼不是 UTF-8，就會進入此處
            # 可在此加入更詳細的日誌或將錯誤的封包寫入檔案以便調查
            print(f"ERROR: Received invalid data from {addr}: {data!r}")

except KeyboardInterrupt:
    # 使用者按 Ctrl+C 時會觸發 KeyboardInterrupt，友善關閉伺服器
    print("\n伺服器關閉。")
finally:
    # 關閉 socket，釋放資源
    server_socket.close()