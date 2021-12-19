import socket

target = "192.168.15.255"
localhost = "127.0.0.1"

def port_scan(target, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((target, port))
        return True
    except:
        return False
print(port_scan(localhost, 80))

for port in range(1, 1024, 1):
    result = port_scan(target, port)
    if result:
        print("port is open")
