import socket
import threading
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server_ip = "192.168.0.103"
server_port = 1234
def send():
    to_send_data = input("Enter what you want to send: ")
    send_data_bytes = to_send_data.encode()
    s.sendto(b"Data incoming" ,(server_ip,server_port))
    s.sendto(send_data_bytes,(server_ip,server_port))
    
def recv():
    data , server = s.recvfrom(1024)
    data = data.decode()
    print(server[0] , ":" , server[1] , ">" , data)

while True:
    try:
        send_data = input("Do you want to send something? (Y/N) ")
        if send_data == "Y":
            send_thread = threading.Thread(target = send())
            send_thread.start()
            recv_thread = threading.Thread(target = recv())
            recv_thread.start()
        else: 
            pass
    except KeyboardInterrupt:
        exit
    