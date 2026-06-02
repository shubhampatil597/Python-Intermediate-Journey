Day 2 - Exception Handling and Debugging

Aim

To study Exception Handling and Debugging in Python.

---

Theory

What is an Exception?

An Exception is an error that occurs during program execution.

Example:

int("abc")

Output:

ValueError

---

Why Exception Handling?

Without exception handling, the program terminates when an error occurs.

Exception handling allows the program to handle errors gracefully and continue execution.

---

try Block

The try block contains code that may generate an exception.

Example:

try:
    num = int(input("Enter Number: "))

---

except Block

The except block handles the exception.

Example:

except ValueError:
    print("Invalid Input")

---

else Block

The else block executes only if no exception occurs.

Example:

else:
    print("Input Accepted")

---

finally Block

The finally block always executes whether an exception occurs or not.

Example:

finally:
    print("Program Finished")

---

raise Keyword

Used to generate exceptions manually.

Example:

age = 15

if age < 18:
    raise ValueError("Age must be 18 or above")

---

Custom Exception

User-defined exceptions can be created by inheriting the Exception class.

Example:

class InvalidTimeError(Exception):
    pass

---

Debugging

Debugging is the process of finding and fixing errors in a program.

Methods:

1. Reading error messages
2. Using print statements
3. Checking program flow

---

Programs Performed

Program 1

Handling ValueError using try and except.

Program 2

Handling ZeroDivisionError.

Program 3

Using else and finally blocks.

Program 4

Creating Custom Exception.

---

Applications

- Cloud Automation Scripts
- API Development
- Monitoring Systems
- Backup Automation
- Production Applications

---

Conclusion

Studied Exception Handling, Debugging Techniques, try, except, else, finally, raise keyword, and Custom Exceptions in Python.