from functools import reduce


costs = [120, 300, 450, 200, 150]


total_cost = reduce(

    lambda x, y: x + y,

    costs

)

print("Total Cost:", total_cost)


high_cost = list(

    filter(

        lambda x: x > 200,

        costs

    )

)

print("\nHigh Cost Resources")

for cost in high_cost:

    print(cost)