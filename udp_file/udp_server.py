import socket
HOST = '0.0.0.0'
PORT = 50005
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((HOST, PORT))
print(f"--- UDP Echo Server (v4) 啟動 ---") 
print("模式: 收到封包 -> 立刻彈回 (Echo)") 
try:
    while True:
        message, address = server_socket.recvfrom(1024)
        server_socket.sendto(message, address) 
    print(f"Error: {e}")
finally:
    server_socket.close()