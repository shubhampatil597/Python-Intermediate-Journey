# Day 11 - Inheritance & Python Mastery

## Overview

Today I learned Inheritance, one of the most important concepts in Object-Oriented Programming (OOP).

Inheritance allows a class to acquire properties and methods from another class, helping reduce code duplication and improve code reusability.

I also explored Python Mastery topics including:

- dataclass
- Type Hints
- Advanced namedtuple
- Advanced OrderedDict

---

# What is Inheritance?

Inheritance is a mechanism that allows one class to inherit attributes and methods from another class.

Example:

Animal → Dog

Dog automatically gets the methods of Animal.

Benefits:

- Code Reusability
- Easy Maintenance
- Better Structure
- Faster Development

---

# Parent Class

A Parent Class provides functionality to other classes.

Example:

```python
class Animal:

    def sound(self):

        print("Animal Sound")
```

---

# Child Class

A Child Class inherits from Parent Class.

Example:

```python
class Dog(Animal):

    pass
```

---

# Types of Inheritance

## Single Inheritance

One Parent → One Child

Example:

Animal → Dog

---

## Multilevel Inheritance

Parent → Child → Grandchild

Example:

Animal → Dog → Puppy

---

## Hierarchical Inheritance

One Parent → Multiple Children

Example:

Animal → Dog

Animal → Cat

Animal → Lion

---

# Method Overriding

A Child Class can replace the method of Parent Class.

Example:

```python
class Dog(Animal):

    def sound(self):

        print("Bark")
```

---

# super() Function

Used to access Parent Class methods and constructors.

Example:

```python
super().__init__()
```

Benefits:

- Reuse Parent Code
- Extend Existing Functionality

---

# dataclass

The dataclass decorator automatically creates:

- __init__()
- __repr__()
- __eq__()

Example:

```python
from dataclasses import dataclass

@dataclass
class Student:

    name:str

    age:int
```

Benefits:

- Less Code
- Cleaner Classes
- Professional Design

---

# Type Hints

Type Hints improve readability and documentation.

Example:

```python
def add(
    a:int,
    b:int
) -> int:

    return a+b
```

Benefits:

- Readable Code
- Better Team Collaboration
- Easier Maintenance

---

# Advanced namedtuple

Useful Features:

## _fields

Returns field names.

## _asdict()

Converts namedtuple into dictionary.

## _replace()

Creates modified copy.

## _make()

Creates object from iterable.

---

# Advanced OrderedDict

Useful Features:

## move_to_end()

Changes order of elements.

## popitem()

Removes items from dictionary.

Applications:

- Deployment Pipelines
- Configuration Management
- Task Scheduling

---

# Mini Project

Employee Management System

Features:

- Parent Class Employee
- Child Classes Developer and Tester
- Method Overriding
- super() Usage
- Code Reusability

---

# Key Concepts Learned

- Inheritance
- Parent Class
- Child Class
- Single Inheritance
- Multilevel Inheritance
- Hierarchical Inheritance
- Method Overriding
- super()
- dataclass
- Type Hints
- Advanced namedtuple
- Advanced OrderedDict

---

# Learning Outcome

By the end of Day 11, I can:

- Create Parent and Child Classes
- Implement Different Types of Inheritance
- Override Methods
- Use super()
- Create dataclasses
- Add Type Hints
- Work with Advanced namedtuple
- Work with Advanced OrderedDict

---

## Author

Shubham Patil

36-Month Cloud Engineer Roadmap Journey

Day 11 - June 2026