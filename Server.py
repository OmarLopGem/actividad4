import socket
import json
import time

host = '127.0.0.1'
port = 65432

serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

x = {}

x = json.dumps(x)

serv.bind((host, port))

serv.listen(5)

while True:
	conn, addr = serv.accept()
	conn.send(b"Processing request ... ")
	data = conn.recv(4096)
	data = data.decode("utf8");
	data = json.loads(data);
	conn.sendall(bytes(x,encoding="utf-8"))
	if not data: break
	print('Last request ...')
	print (data)