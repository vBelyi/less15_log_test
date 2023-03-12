import logging
import socket


logging.basicConfig(level=logging.DEBUG, filename='py_log.log', filemode='w', format='%(asctime)s %(levelname)s: %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

sock_server = socket.socket()
sock_server.settimeout(10)

sock_server.bind(('127.0.0.1', 80))
sock_server.listen()
logging.info('Socket opened successfully')

while True:
    try:
        conn, add = sock_server.accept()
    except socket.timeout:
        logging.warning("Client is still not connected")
        continue

    name = 'AI'
    client = (conn.recv(1024)).decode()
    logging.info(f'Connected to {client}')
    print('connected ' + client)
    conn.send(name.encode())

    timeout = 20
    conn.settimeout(timeout)
    while True:
        data = input('AI: ')
        conn.send(data.encode())
        try:
            data = conn.recv(1024)
            data = data.decode()
            logging.info(f'{client}: {data}')
            print(client, ':', data)
        except socket.timeout:
            logging.error('Client is not responding. Server is closed')
            sock_server.close()
            break




