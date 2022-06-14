import string
import itertools
import socket
import sys

args = sys.argv
hostname = args[1]
port = int(args[2])
ascii_lowercase = string.ascii_lowercase
digits = string.digits
symbols = itertools.chain(ascii_lowercase, digits)
status = 'WRONG'
i = 1

with socket.socket() as client_socket:
    address = (hostname, port)
    client_socket.connect(address)
    while status != 'Connection success!':
        password = itertools.product(itertools.chain(ascii_lowercase, digits), repeat=i)
        for j in range(len(list(itertools.product(itertools.chain(ascii_lowercase, digits), repeat=i)))):
            message = ''.join(next(password))
            message_origin = message
            message = message.encode("utf-8")
            client_socket.send(message)
            response = client_socket.recv(1024)
            response = response.decode("utf-8")
            if response == 'Connection success!':
                status = 'Connection success!'
                print(message_origin)
                break
        i += 1
