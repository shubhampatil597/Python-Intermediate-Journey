def large_dataset():

    for num in range(1000000):

        yield num


data = large_dataset()

for _ in range(5):

    print(next(data))