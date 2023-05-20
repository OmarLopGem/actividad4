import socket
import json
import time

host = '127.0.0.1'
port = 65432

serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

secs = 10

x = {}
x = json.dumps(x)

serv.bind((host, port))

serv.listen(5)

serv.settimeout(4)

start_time = time.time()
end_time = start_time + 60

tasks_list=[]

while True:
    try:
        serv.settimeout(end_time - time.time())
        print('Waiting for connection ... ')
        conn, addr = serv.accept()
        print('Connection from: ', addr)
        conn.send(b"Processing request ... ")
        data = conn.recv(4096)
        data = data.decode("utf8")
        data = json.loads(data)
        
        tasks_list.append({'task': data['task'], 'cpu': data['cpu']})
        
        conn.sendall(bytes(x, encoding="utf-8"))
        if not data:
            break
        print('Last request ...')
        print(data)
        print(x)

    except socket.timeout:
        print('Time out')
        break

tasks_list.sort(key=lambda task: task['cpu'])
sorted_tasks = [task['task'] for task in tasks_list]
for task in sorted_tasks:
    print(task)
