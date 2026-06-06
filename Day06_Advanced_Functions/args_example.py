# Using *args

def add(*numbers):

    total = 0

    for num in numbers:
        total += num

    return total

print("Sum =", add(10, 20))
print("Sum =", add(10, 20, 30))
print("Sum =", add(10, 20, 30, 40))