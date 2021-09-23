import time
import socket

class Client :
    def __init__(self, arg_sock: tuple, reader: callable = None):
        self.sock = socket.socket()
        self.sock.connect(arg_sock)
        self.receive_flag = True
        self.reader = reader

    def receive(self):
        while self.receive_flag :
            data = self.sock.recv(2048).decode()
            if self.reader : self.reader(data)
            time.sleep(0.01)

    def __del__(self):
        self.receive_flag = False
        self.sock.close()

