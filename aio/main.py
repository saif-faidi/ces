from network.tcp_client import Client
from conf import aio_socket
import json

def reader(data):
    try :
        data = json.loads(data)
        print(data)
    except Exception :
        print('error: ',len(data), data)



if __name__ == "__main__":
    tcp_client = Client(aio_socket, reader)
    tcp_client.receive()