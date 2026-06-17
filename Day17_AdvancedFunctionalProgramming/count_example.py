from itertools import count

counter = count(

    start=100,

    step=10

)

for _ in range(5):

    print(next(counter))