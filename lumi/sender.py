
import json
from color import Color


class Sender:
    def __init__(self,client):
        self.client = client

    def send(self,color : Color):
        self.client.send(json.dumps(color.to_json()))




