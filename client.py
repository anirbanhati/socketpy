import socket
import pickle
header=10
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((socket.gethostname(),1234))
while True:
    fm=""
    newmsg=True
    while True:
        msg = s.recv(1024)
        if newmsg:
            print(f"new message length={msg[:header]}")
            msln=int(msg[:header])
            newmsg=False
        fm+=msg.decode("utf-8")
        if(len(fm)-header==msln):
            print('full message received')
            print(fm[header:])
            print(pickle.loads(fm[header:]))
            newmsg=True
            fm=b''
    print(fm)
