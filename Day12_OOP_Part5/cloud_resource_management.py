from enum import Enum


class ResourceState(Enum):

    RUNNING = 1
    STOPPED = 2


class Resource:

    def __init__(self, name, state):

        self.name = name
        self.state = state

    def start(self):

        print("Resource Started")

    def __str__(self):

        return f"{self.name} - {self.state.name}"


class WebServer(Resource):

    def start(self):

        print(f"{self.name} Web Server Started")


class DatabaseServer(Resource):

    def start(self):

        print(f"{self.name} Database Started")


resources = [

    WebServer(
        "WEB-01",
        ResourceState.RUNNING
    ),

    DatabaseServer(
        "DB-01",
        ResourceState.STOPPED
    )

]


for resource in resources:

    print(resource)

    resource.start()