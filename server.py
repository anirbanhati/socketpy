import socket
import time
import pickle
def main():
    header=10
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind((socket.gethostname(),1234))
    s.listen(5)
    while True:
        clientsocket,adress=s.accept()
        print(f"{adress}::connected")
        msg="welcome to server"
        msg=f'{len(msg):<{header}}'+msg
        dob={"day":28,"mon":6,"year":95}
        dmsg=pickle.dumps(dob)
        dmsg=bytes(f"{len(dmsg):<{header}}",'utf-8')+dmsg
        clientsocket.send(bytes(msg,"utf-8"))
        clientsocket.send(dmsg)
        while True:
            time.sleep(2)
            msg=f"time={time.time()}"
            msg=f'{len(msg):<{header}}'+msg
            clientsocket.send(bytes(msg,"utf-8"))
if __name__=='__main__':
    main()