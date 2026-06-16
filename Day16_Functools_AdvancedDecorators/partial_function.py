from functools import partial


def multiply(x, y):

    return x * y


double = partial(

    multiply,

    2

)

print("Double of 10:", double(10))

print("Double of 25:", double(25))