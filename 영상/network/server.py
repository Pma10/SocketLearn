from socket import *
from threading import Thread
import network.common as common

class Server:
    def __init__(self, host="0.0.0.0", port=9999):
        self.socket = socket()
        self.socket.bind((host, port))
        self.socket.listen()

    def run(self, fun, **kwargs):
        while True:
            client, address = self.socket.accept()
            Thread(target=fun, args=(client, address, kwargs)).start()

    def __del__(self):
        self.socket.close()

    def recv(self, client):
        return client.recv(common.BUF_SIZE)

    def send(self, client, data):
        client.send(data)
