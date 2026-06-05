# Multiple Return Values Example

def calculation(a, b):
    return a + b, a - b

addition, subtraction = calculation(20, 10)

print("Addition =", addition)
print("Subtraction =", subtraction)