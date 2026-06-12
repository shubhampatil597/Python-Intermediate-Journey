class Server:

    def deploy(self):

        print("Server Deployed")


class Container:

    def deploy(self):

        print("Container Deployed")


def deploy_resource(resource):

    resource.deploy()


deploy_resource(Server())

deploy_resource(Container())