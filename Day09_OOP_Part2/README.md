# Day 9 - OOP Part 2 (Methods, Class Variables, Class Methods and Static Methods)

## Overview

Today I continued my Object-Oriented Programming (OOP) journey by learning how objects perform actions using methods and how data can be shared across all objects using class variables.

I also learned the difference between instance methods, class methods, and static methods, which are commonly used in professional Python applications.

Additionally, I explored the object lifecycle and learned how objects are created and destroyed in Python.

---

# Learning Objectives

By completing Day 9, I learned:

- Methods in Python Classes
- Instance Methods
- Class Variables
- Class Methods
- Static Methods
- Object Lifecycle
- Destructor (__del__)
- Real-world OOP Design

---

# What is a Method?

A method is a function defined inside a class.

Methods allow objects to perform actions.

Example:

```python
class Student:

    def greet(self):
        print("Hello Student")
```

Methods help combine data and behavior into a single unit.

---

# Instance Methods

Instance methods work with object-specific data.

They use:

```python
self
```

Example:

```python
class Student:

    def __init__(self,name):
        self.name = name

    def display(self):
        print(self.name)
```

Each object can display its own information.

---

# Class Variables

Class variables belong to the class itself.

They are shared among all objects.

Example:

```python
class Student:

    college = "D Y Patil College"
```

Every object can access this variable.

Benefits:

- Memory efficient
- Shared information
- Easy updates

---

# Class Methods

Class methods operate on class-level data.

They use:

```python
@classmethod
```

and

```python
cls
```

Example:

```python
class Student:

    college = "D Y Patil College"

    @classmethod
    def show_college(cls):
        print(cls.college)
```

---

# Static Methods

Static methods do not depend on:

- Object data
- Class data

They are utility functions placed inside a class.

Example:

```python
class Student:

    @staticmethod
    def is_adult(age):
        return age >= 18
```

---

# Difference Between Methods

| Type | Uses |
|--------|--------|
| Instance Method | Object Data |
| Class Method | Class Data |
| Static Method | Utility Functions |

---

# Object Lifecycle

Every object follows:

1. Creation
2. Usage
3. Destruction

Creation:

```python
s1 = Student()
```

Destruction:

```python
del s1
```

Destructor:

```python
__del__()
```

---

# Mini Project

Library Management System

Features:

- Library Name
- Book Count
- Shared College Name
- Validation using Static Method
- Information Display

---

# Real World Applications

These concepts are widely used in:

- Cloud Engineering
- DevOps Automation
- Django Applications
- Flask Applications
- AWS SDK
- Infrastructure Management Tools

---

# Key Concepts Learned

- Method
- Instance Method
- Class Variable
- Class Method
- Static Method
- Object Lifecycle
- Destructor

---

# Learning Outcome

By the end of Day 9, I can:

- Create methods in classes
- Use instance methods
- Use class variables
- Use class methods
- Use static methods
- Understand object lifecycle
- Design better OOP structures

---

## Author

Shubham Patil

36-Month Cloud Engineer Roadmap Journey

Day 9 - June 2026