from functools import lru_cache


@lru_cache
def square(num):

    print("Calculating...")

    return num * num


print(square(5))

print(square(5))

print(square(10))

print(square(10))