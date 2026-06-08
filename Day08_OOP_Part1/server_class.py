class Server:

    def __init__(self, name, ip):

        self.name = name
        self.ip = ip

server1 = Server(
    "Web Server",
    "192.168.1.10"
)

server2 = Server(
    "Database Server",
    "192.168.1.20"
)

print("Server Details")
print("--------------------")

print(server1.name, "-", server1.ip)
print(server2.name, "-", server2.ip)