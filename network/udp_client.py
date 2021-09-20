import socket
from threading import Thread
import time

class Client:

    def __init__(self,argIp,argPort):
        self.targetServertIp     = argIp
        self.targetServertPort   = argPort
        self.targetServer        =  (self.targetServertIp , self.targetServertPort)
        self.receivingFlag       = True
        self.receptionThread     = Thread(target= self.receive)
        self.socketInstance      = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


    def receive(self):
        while self.receivingFlag:
            data = self.socketInstance.recv(1024).decode()
            print(data)
            time.sleep(0.01)

    def send(self,data):
        self.socketInstance.sendto(data.encode(), self.targetServer)

    def startReception(self):
        self.receptionThread.start()

    def stopReception(self):
        self.receivingFlag = False
        self.receptionThread.join()

    def __del__(self):
        self.socketInstance.close()
