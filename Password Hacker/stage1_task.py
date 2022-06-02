import socket
import sys

args = sys.argv
hostname = args[1]
port = int(args[2])
message = args[3]

with socket.socket() as client_socket:
    address = (hostname, port)
    client_socket.connect(address)
    message = message.encode()
    client_socket.send(message)
    response = client_socket.recv(1024)
    response = response.decode()
    print(response)
