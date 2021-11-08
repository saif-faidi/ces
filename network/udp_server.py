import socket
from threading import Thread
import time
class Server():

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
        print("started receiving")
        while self.receivingFlag:
            data,addr = self.socketInstance.recvfrom(1024)
            data      = data.decode()
            self.clientAddress  = addr
            print("received = ", data)
            time.sleep(0.005)

    def send(self,data):
        #check if there is already a message received from the client
        #in order to get it's address
        self.socketInstance.sendto(data.encode(), self.clientAddress)

    def startReception(self):
        self.receptionThread.start()

    def stopReception(self):
        print('Reception Stopped')
        self.receivingFlag = False
        self.receptionThread.join()
        self.socketInstance.close()


