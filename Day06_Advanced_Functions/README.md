# Day 6 - Advanced Functions

## Aim

To study *args, **kwargs, Lambda Functions, List Comprehensions, Dictionary Comprehensions, and Set Comprehensions in Python.

---

## Theory

### *args

*args allows a function to accept multiple positional arguments.

Example:

def add(*numbers):
    print(numbers)

add(10,20,30)

Output:

(10,20,30)

---

### **kwargs

**kwargs allows a function to accept multiple keyword arguments.

Example:

def student(**details):
    print(details)

student(name="Shubham", age=20)

Output:

{'name':'Shubham','age':20}

---

### Lambda Function

A lambda function is an anonymous function.

Example:

square = lambda x: x*x

print(square(5))

Output:

25

---

### List Comprehension

Used to create lists in a shorter way.

Example:

numbers = [x for x in range(5)]

Output:

[0,1,2,3,4]

---

### Dictionary Comprehension

Used to create dictionaries efficiently.

Example:

data = {x:x*x for x in range(5)}

Output:

{0:0,1:1,2:4,3:9,4:16}

---

### Set Comprehension

Used to create sets efficiently.

Example:

data = {x*x for x in range(5)}

Output:

{0,1,4,9,16}

---

## Programs Performed

### Program 1
Using *args

### Program 2
Using **kwargs

### Program 3
Lambda Function for Square

### Program 4
Lambda Function for Addition

### Program 5
List Comprehension

### Program 6
Dictionary Comprehension

### Program 7
Set Comprehension

### Program 8
CPU Monitoring Data Processing

---

## Applications

- Data Processing
- Automation Scripts
- Cloud Monitoring
- Log Analysis
- API Response Processing
- DevOps Tools

---

## Conclusion

Studied *args, **kwargs, Lambda Functions, List Comprehensions, Dictionary Comprehensions, and Set Comprehensions in Python.