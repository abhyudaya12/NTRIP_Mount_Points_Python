

import socket

UserAgent = 'MountPointScript'


Server = '210.117.198.83'
Port = 2101



client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = (Server, Port)
client_socket.connect(server_address)

request_header = ("GET / HTTP/1.1\r\n" +
    "User-Agent: NTRIP Client/1.0\r\n" +
    "Connection: close\r\n" +
    "\r\n")

print("**********************")
print("*  request_header    *")
print("**********************")
print(request_header)

request_header = bytes(request_header, encoding='utf-8')
client_socket.send(request_header)

response = b''
while True:
    recv = client_socket.recv(1024)
    if not recv:
        break
    response += recv 

print("**********************")
print("*     response       *")
print("**********************")

# response contains a bunch of '\r\n' terminated lines
response = str(response, 'UTF-8')
print (response)
client_socket.close()
