import socket
from threading import Thread

from typing import List

import time
class Server:

    def __init__(self,argIp : str,argPort : int):
        self.ip                         = argIp
        self.port                       = argPort
        self.address                    = (self.ip , self.port)
        self.receivingFlag              = True
        self.socketInstance             = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.receptionThread            = Thread(target= self.receive)
        self.receptionThread.setDaemon(True)
        self.clientAddress              = ()

    def bind(self):
        self.socketInstance.bind(self.address)

    def receive(self):
        while self.receivingFlag:
            data,addr = self.socketInstance.recvfrom(1024)
            data      = data.decode()
            self.clientAddress  = addr
            print(data)


    def send(self,data):
        self.socketInstance.sendto(data.encode(), self.clientAddress)

    def startReception(self):
        self.receptionThread.start()

    def stopReception(self):
        print('Reception Stopped')
        self.receivingFlag = False
        #self.receptionThread.join()
        self.socketInstance.close()


    def __del__(self):
        self.stopReception()


if __name__ == '__main__':
    server = Server('127.0.0.1', 6799)
    server.bind()
    print("Listeneing on socket : 127.0.1.1:6799 ")
    server.receive()