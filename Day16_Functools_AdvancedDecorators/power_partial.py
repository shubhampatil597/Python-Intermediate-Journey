from functools import partial


def power(base, exponent):

    return base ** exponent


square = partial(

    power,

    exponent=2

)

cube = partial(

    power,

    exponent=3

)

print("Square:", square(5))

print("Cube:", cube(5))