servers = [

    {"name": "Server1", "cpu": 80},

    {"name": "Server2", "cpu": 30},

    {"name": "Server3", "cpu": 60}

]

servers.sort(

    key=lambda x: x["cpu"]

)

print(servers)