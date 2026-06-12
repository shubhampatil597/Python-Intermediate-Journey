# Day 12 - Polymorphism & Python Mastery

## Overview

Today I learned Polymorphism, one of the four major pillars of Object-Oriented Programming.

Polymorphism allows the same interface to behave differently depending on the object using it.

I also explored advanced Python concepts including:

- Duck Typing
- Operator Overloading
- Magic Methods
- Enum
- pathlib

These concepts are widely used in professional software development, automation tools, cloud platforms, and DevOps applications.

---

# What is Polymorphism?

Polymorphism means:

Many Forms

The same method can perform different actions depending on the object.

Example:

```python
dog.sound()

cat.sound()
```

Both use:

```python
sound()
```

But produce different outputs.

---

# Benefits of Polymorphism

- Flexible Code
- Reusable Design
- Easy Maintenance
- Better Scalability
- Professional Architecture

---

# Runtime Polymorphism

Runtime Polymorphism occurs through Method Overriding.

Example:

```python
class Vehicle:

    def start(self):

        print("Vehicle Started")


class Car(Vehicle):

    def start(self):

        print("Car Started")
```

The method is selected during program execution.

---

# Duck Typing

Python focuses on behavior instead of type.

Principle:

"If it behaves like a duck, it is treated like a duck."

Example:

```python
class Dog:

    def speak(self):

        print("Bark")


class Cat:

    def speak(self):

        print("Meow")
```

Function:

```python
def make_sound(animal):

    animal.speak()
```

No type checking required.

---

# Operator Overloading

Operators can be customized for user-defined classes.

Example:

```python
class Number:

    def __add__(self,other):

        return self.value + other.value
```

Allows:

```python
n1 + n2
```

to behave according to our logic.

---

# Magic Methods

Magic Methods are special methods automatically called by Python.

Common Examples:

```python
__init__()

__str__()

__add__()

__len__()

__repr__()
```

---

## __init__()

Constructor Method

Used when object is created.

---

## __str__()

Controls object printing.

Example:

```python
print(object)
```

---

## __add__()

Controls + operator behavior.

---

# Enum

Enum represents a fixed set of constants.

Example:

```python
from enum import Enum

class Status(Enum):

    RUNNING = 1

    STOPPED = 2

    FAILED = 3
```

Benefits:

- Prevents Typing Errors
- Improves Readability
- Creates Consistent Values

---

# pathlib

Modern way of handling files and folders.

Example:

```python
from pathlib import Path
```

Common Operations:

```python
Path.cwd()

Path.home()

mkdir()

touch()

exists()
```

Benefits:

- Cleaner Syntax
- Cross Platform
- Easy File Management

---

# Mini Project

Cloud Resource Management System

Features:

- Polymorphism
- Method Overriding
- Enum
- Magic Methods
- Cloud Resource Simulation

---

# Key Concepts Learned

- Polymorphism
- Runtime Polymorphism
- Duck Typing
- Operator Overloading
- Magic Methods
- __init__()
- __str__()
- __add__()
- Enum
- pathlib

---

# Learning Outcome

By the end of Day 12, I can:

- Implement Polymorphism
- Apply Duck Typing
- Override Methods
- Overload Operators
- Use Magic Methods
- Create and Use Enums
- Manage Files with pathlib
- Build Flexible Object-Oriented Programs

---

## Author

Shubham Patil

36-Month Cloud Engineer Roadmap Journey

Day 12 - June 2026