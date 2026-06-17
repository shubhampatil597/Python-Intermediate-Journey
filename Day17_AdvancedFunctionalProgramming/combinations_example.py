from itertools import combinations

servers = [

    "Server1",

    "Server2",

    "Server3",

    "Server4"

]

pairs = combinations(

    servers,

    2

)

for pair in pairs:

    print(pair)