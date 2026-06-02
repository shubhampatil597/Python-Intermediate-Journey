#Day 2 - Exception Handling Examples

print("Example 1 : ValueError")

try:
number = int(input("Enter a Number: "))
print("You entered:", number)

except ValueError:
print("Invalid Input! Numbers only.")

print("\n---------------------")

print("Example 2 : ZeroDivisionError")

try:
num = int(input("Enter Number: "))
result = 100 / num

except ZeroDivisionError:
print("Cannot divide by zero")

else:
print("Result =", result)

finally:
print("Program Finished")