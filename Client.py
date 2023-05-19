import socket
import json
import argparse
import datetime

parser = argparse.ArgumentParser(description='MOAB-Torque')
parser.add_argument('--walltime', type=int, required = True, help='Enter walltime type int')
parser.add_argument('--mempeak', type=str, required = True, help='Enter mempeak #gb')
parser.add_argument('--cpu', type=int, required = True, help='Enter cores to be used')
parser.add_argument('--task', type=str, required = True, help='Enter task to be done')


args = parser.parse_args()

current_time = datetime.datetime.now();
current_time = current_time.strftime("%D %H:%M:%S");

x = {
  "walltime": args.walltime,
  "mempeak": args.mempeak,
  "cpu": args.cpu,
  "task": args.task,
  "Date": current_time
}

print(x)

x = json.dumps(x)

host = '127.0.0.1' 
port = 65432


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

ack = client.recv(4096)
print (ack)

client.sendall(bytes(x,encoding="utf-8"))
data = client.recv(4096)
data = data.decode("utf8");
data = json.loads(data)

print(data)