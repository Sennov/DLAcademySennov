import socket
import time
import threading
import json


# чат

HOST = 'localhost'
PORT = 9090

clients = []

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((HOST, PORT))
print('[Server started')
quit = False

while not quit:
    try:
        data, addr = s.recvfrom(1024)
        encoded_data = json.loads(data.decode("utf-8"))
        name = encoded_data['name']
        message = encoded_data['message']

        if addr not in clients:
            clients.append(addr)

        itsatime = time.strftime('%Y-%m-%d - %H^%M', time.localtime())

        print("[" + addr[0] + "]=[" + str(addr[1]) + "]=[" + itsatime + "]/", end="")
        print('[' + name + '] :: ' + message)
        for client in clients:
            if addr !=client:
                s.sendto(data, client)
    except Exception as ex:
        print(ex)
        print("\n [ Server Stopped ]")

s.close()

