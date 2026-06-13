def numbers():

    yield 1

    yield 2

    yield 3

    yield 4


gen = numbers()

for value in gen:

    print(value)