# Day 8 - Object Oriented Programming (OOP) Part 1

## Overview

Today I started learning Object-Oriented Programming (OOP) in Python. OOP is one of the most important programming paradigms used in software development, cloud engineering, web applications, automation, and enterprise systems.

Instead of storing data in separate variables, OOP allows us to create objects that contain both data and behavior.

This helps developers write scalable, reusable, and maintainable code.

---

# Why OOP is Needed

Consider storing student information using normal variables:

```python
student1_name = "Shubham"
student1_age = 20

student2_name = "Ram"
student2_age = 18
```

This works for a few students.

However, if we need to store information for hundreds or thousands of students, managing variables becomes difficult.

OOP solves this problem by creating objects.

---

# What is a Class?

A Class is a blueprint or template used to create objects.

Example:

```python
class Student:
    pass
```

The above class does not create any student.

It only creates a blueprint.

---

# What is an Object?

An Object is an instance of a class.

Example:

```python
s1 = Student()
```

Here:

- Student = Class
- s1 = Object

Objects are real entities created using a class.

---

# Constructor

A Constructor is a special method that executes automatically when an object is created.

Python Constructor:

```python
__init__()
```

Example:

```python
class Student:

    def __init__(self):
        print("Student Created")
```

Whenever an object is created, the constructor runs automatically.

---

# Understanding self

self refers to the current object.

Example:

```python
class Student:

    def __init__(self,name):
        self.name = name
```

self allows each object to store its own data.

---

# Instance Variables

Variables that belong to an object are called Instance Variables.

Example:

```python
class Student:

    def __init__(self,name,age):

        self.name = name
        self.age = age
```

Each object stores its own values.

---

# Real World Example

Class:

```text
Car
```

Objects:

```text
BMW
Audi
Mercedes
```

Another Example:

Class:

```text
Student
```

Objects:

```text
Shubham
Ram
Shyam
```

---

# Cloud Engineering Example

Class:

```text
Server
```

Objects:

```text
Web Server
Database Server
Backup Server
```

Each server can have:

- Name
- IP Address
- CPU
- RAM
- Status

This is how cloud systems are modeled using OOP.

---

# Programs Implemented

1. Class Example
2. Constructor Example
3. Student Class
4. Server Class
5. Collections Module Examples

---

# Key Concepts Learned

- OOP
- Class
- Object
- Constructor
- self
- Instance Variables
- Counter
- defaultdict
- deque

---

# Learning Outcome

By the end of Day 8, I learned:

- Why OOP exists
- How classes are created
- How objects are created
- How constructors work
- How instance variables store data
- How self works
- Basic cloud infrastructure modeling using OOP

---

# Cloud Engineer Roadmap Progress

Month: June 2026

Completed Topics:

- Modules & Packages
- Exception Handling
- File Handling
- CSV Processing
- JSON Processing
- Data Processing
- Functions
- Lambda Functions
- Comprehensions
- Environment Management
- Type Hints
- Dataclasses
- OOP Part 1

---

## Author

Shubham Patil

36-Month Cloud Engineer Roadmap Journey

Day 8 - June 2026