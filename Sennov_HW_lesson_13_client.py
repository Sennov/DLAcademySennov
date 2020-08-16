import socket
import time
import threading
import json
import Sennov_HW_lesson_13_log_config


# клиент чата

shutdown = False
join = False
log = Sennov_HW_lesson_13_log_config.log
def receiving(s):
    global shutdown
    while not shutdown:
        try:
            while True:
                data, addr = s.recvfrom(1024)
                encoded_data = json.loads(data.decode("utf-8"))
                name = encoded_data['name']
                message = encoded_data['message']
                print('[' + name + '] :: ' + message)
                time.sleep(0.2)
        except:
            pass

def sending(name, s):
    global shutdown
    global join
    while not shutdown:
        if not join:
            data = {'name': name,
                    'message': 'join chat'
                    }
            log.info(f'{data["name"]} join chat')
            s.sendto(json.dumps(data).encode("utf-8"), server)
            join = True
        else:
            try:
                message = input("[You] :: ")
                data = {'name': name,
                        'message': message
                        }
                if message !="":
                    s.sendto(json.dumps(data).encode("utf-8"), server)
                    log.info(f'{data["name"]} sent message')
                time.sleep(0.2)
            except:
                data = {'name': name,
                        'message': 'left chat'}
                s.sendto(json.dumps(data).encode("utf-8"), server)
                log.info(f'{data["name"]} left chat')
                shutdown = True

server = ('localhost', 9090)
name = input("Name: ")
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(server)

rT = threading.Thread(target=receiving, args=(s, ))
sT = threading.Thread(target=sending, args=(name, s))

rT.start()
sT.start()
rT.join()
sT.join()
s.close()
