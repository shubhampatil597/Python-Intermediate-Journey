from itertools import permutations

servers = [

    "A",

    "B",

    "C"

]

result = permutations(

    servers,

    2

)

for item in result:

    print(item)