cache = {}


def square(num):

    if num in cache:

        print("From Cache")

        return cache[num]

    print("Calculating")

    result = num * num

    cache[num] = result

    return result


print(square(5))

print(square(5))