from itertools import product

regions = [

    "Mumbai",

    "Pune"

]

services = [

    "Web",

    "Database"

]

result = product(

    regions,

    services

)

for item in result:

    print(item)