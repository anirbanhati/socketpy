import socket
import time
import pickle
HEADERSIZE = 10
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1243))
s.listen(5)
while True:
    clientsocket,adress=s.accept()
    print(f"{adress}::connected")
    dob={"day":28,"mon":6,"year":95}
    dmsg=pickle.dumps(dob)
    dmsg=bytes(f"{len(dmsg):<{HEADERSIZE}}",'utf-8')+dmsg
    clientsocket.send(dmsg)
    while True:
        time.sleep(2)
        clientsocket.send(dmsg)