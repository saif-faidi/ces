from network.tcp_client import Client
from conf import aio_socket
import json

def reader(data):
    #data = json.loads(data)
    print(data)

if __name__ == "__main__":
    tcp_client = Client(aio_socket, reader)
    tcp_client.receive()