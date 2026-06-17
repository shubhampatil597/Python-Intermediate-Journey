def countdown():

    yield 5

    yield 4

    yield 3

    yield 2

    yield 1


for number in countdown():

    print(number)