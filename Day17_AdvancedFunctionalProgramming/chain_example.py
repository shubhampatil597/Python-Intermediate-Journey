from itertools import chain

frontend_servers = [

    "Web-1",

    "Web-2"

]

backend_servers = [

    "API-1",

    "API-2"

]

all_servers = chain(

    frontend_servers,

    backend_servers

)

for server in all_servers:

    print(server)