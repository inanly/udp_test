# udp_client.py (RTT Version)
import socket
import time
import sys

# 1. Read target IP (if no argument provided, default to localhost, but we'll pass it in K8s)
SERVER_IP = sys.argv[1] if len(sys.argv) > 1 else '127.0.0.1'
SERVER_PORT = 50005

print(f"--- [Client] RTT Performance Test ---")
print(f"Target server: {SERVER_IP}:{SERVER_PORT}")

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.settimeout(2.0) # 2 second timeout for packet loss detection

packet_count = 50   # Test 50 packets
rtt_list = []

try:
    for i in range(packet_count):
        start_time = time.time() # Record departure time (T1)
        message = f"seq-{i}".encode()
        
        try:
            # Send
            client_socket.sendto(message, (SERVER_IP, SERVER_PORT))
            
            # Wait for response (Echo)
            data, server = client_socket.recvfrom(1024)
            
            end_time = time.time()   # Record arrival time (T2)
            
            # Calculate RTT
            rtt = (end_time - start_time) * 1000
            rtt_list.append(rtt)
            print(f"Seq {i}: RTT = {rtt:.3f} ms")
            
        except socket.timeout:
            print(f"Seq {i}: Request timeout (packet loss)")
        except Exception as e:
            print(f"Seq {i}: Error {e}")
            
        # Simulate real-time transmission frequency (e.g., 50Hz = 0.02s)
        time.sleep(0.02) 

except KeyboardInterrupt:
    print("User stopped")
finally:
    client_socket.close()

# Display statistics
if rtt_list:
    avg_rtt = sum(rtt_list) / len(rtt_list)
    print("==================================")
    print(f"Succeeded. Average latency: {avg_rtt:.3f} ms")
    print("==================================")