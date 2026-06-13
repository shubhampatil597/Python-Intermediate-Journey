from abc import ABC
from abc import abstractmethod


class Resource(ABC):

    @abstractmethod
    def deploy(self):

        pass


class Server(Resource):

    def deploy(self):

        print("Server Deployed")


server = Server()

server.deploy()