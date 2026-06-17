from itertools import cycle

servers = cycle(

    [

        "Server-A",

        "Server-B",

        "Server-C"

    ]

)

for _ in range(10):

    print(next(servers))