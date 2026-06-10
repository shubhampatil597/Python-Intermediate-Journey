# Day 10 - OOP Part 3 (Encapsulation & Data Hiding)

## Overview

Today I learned one of the most important concepts in Object-Oriented Programming (OOP): Encapsulation.

Encapsulation helps protect data from direct access and ensures that object data is modified only through controlled methods.

I also explored advanced collections from Python's collections module including namedtuple, OrderedDict, and ChainMap.

---

# What is Encapsulation?

Encapsulation is the process of combining data and methods into a single unit while controlling access to that data.

It helps:

- Protect sensitive information
- Prevent accidental modifications
- Improve code maintainability
- Improve software security

---

# Data Hiding

Data Hiding prevents direct access to important variables.

Example:

Instead of:

```python
account.balance = 100000
```

We use:

```python
account.deposit()
account.withdraw()
```

This ensures proper validation and security.

---

# Public Members

Public members are accessible from anywhere.

Example:

```python
self.name
```

Usage:

```python
student.name
```

---

# Protected Members

Protected members use a single underscore.

Example:

```python
self._age
```

They are intended for internal use.

---

# Private Members

Private members use double underscores.

Example:

```python
self.__password
```

These members cannot be accessed directly outside the class.

---

# Getter Methods

Getter methods safely read private data.

Example:

```python
def get_balance(self):
    return self.__balance
```

---

# Setter Methods

Setter methods safely modify private data.

Example:

```python
def set_balance(self, amount):
    if amount > 0:
        self.__balance = amount
```

---

# Advanced Collections

## namedtuple

Provides named fields for tuples.

Advantages:

- Readable
- Fast
- Memory Efficient

---

## OrderedDict

Maintains dictionary insertion order and provides additional ordering features.

---

## ChainMap

Combines multiple dictionaries into one logical view.

---

# Mini Project

Bank Account Management System

Features:

- Private Balance
- Deposit Function
- Withdraw Function
- Balance Validation
- Encapsulation
- Data Hiding

---

# Key Concepts Learned

- Encapsulation
- Data Hiding
- Public Members
- Protected Members
- Private Members
- Getters
- Setters
- namedtuple
- OrderedDict
- ChainMap

---

# Learning Outcome

By the end of Day 10, I can:

- Protect object data
- Hide sensitive information
- Create getter methods
- Create setter methods
- Use advanced collections
- Design secure OOP applications

---

## Author

Shubham Patil

36-Month Cloud Engineer Roadmap Journey

Day 10 - June 2026