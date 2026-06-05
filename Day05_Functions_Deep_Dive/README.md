# Day 5 - Functions Deep Dive

## Aim

To study Functions, Parameters, Arguments, Return Values, Default Arguments, Keyword Arguments, and Variable Scope in Python.

---

## Theory

### What is a Function?

A function is a block of reusable code designed to perform a specific task.

Example:

def greet():
    print("Hello")

greet()

Benefits:
- Code Reusability
- Better Organization
- Easy Maintenance
- Reduced Code Duplication

---

### Function with Parameters

Parameters allow functions to receive data.

Example:

def greet(name):
    print("Hello", name)

greet("Shubham")

---

### Return Statement

The return statement sends a value back to the caller.

Example:

def add(a,b):
    return a+b

result = add(10,20)

print(result)

Output:

30

---

### Default Arguments

Default values are used when no argument is passed.

Example:

def greet(name="Guest"):
    print("Hello", name)

greet()

Output:

Hello Guest

---

### Keyword Arguments

Arguments can be passed using parameter names.

Example:

def student(name, age):
    print(name, age)

student(age=20, name="Shubham")

---

### Local Variables

Variables declared inside a function.

Example:

def demo():
    x = 10
    print(x)

demo()

---

### Global Variables

Variables declared outside a function.

Example:

name = "Shubham"

def show():
    print(name)

show()

---

### Variable Scope

Local Scope:
- Accessible only inside the function.

Global Scope:
- Accessible throughout the program.

---

### Multiple Return Values

Example:

def calculation(a,b):
    return a+b, a-b

add, sub = calculation(20,10)

print(add)
print(sub)

Output:

30
10

---

## Programs Performed

### Program 1
Simple Function

### Program 2
Function with Parameters

### Program 3
Function with Return Value

### Program 4
Default Arguments

### Program 5
Keyword Arguments

### Program 6
Local and Global Variables

### Program 7
Multiple Return Values

---

## Applications

- Cloud Automation Scripts
- Monitoring Tools
- API Processing
- Log Analysis
- DevOps Automation
- Data Processing

---

## Conclusion

Studied Functions, Parameters, Return Values, Default Arguments, Keyword Arguments, Variable Scope, and Multiple Return Values in Python.