def multiplier(x):

    def multiply(y):

        return x * y

    return multiply


double = multiplier(2)

print(double(10))

triple = multiplier(3)

print(triple(10))