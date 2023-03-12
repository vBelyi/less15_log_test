import socket

sock1 = socket.socket()

print('Chat is open')
name = input('Print your name: ')
sock1.connect(('127.0.0.1', 80))
sock1.send(name.encode())
socket_name = sock1.recv(1024)
server_name = socket_name.decode()
print(server_name, 'connected')

while True:
    data = (sock1.recv(1024)).decode()
    print(server_name, ':', data)
    data = input(f'Client {name}: ')
    sock1.send(data.encode())