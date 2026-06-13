# Day 13 - Abstraction, ABC Module, Iterators & Generators

## Overview

Today I learned Abstraction, one of the most important Object-Oriented Programming principles.

Abstraction focuses on hiding implementation details and exposing only the necessary functionality to users.

I also learned:

- Abstract Classes
- Abstract Methods
- ABC Module
- Interface Design
- Iterators
- Generators
- yield Keyword
- Lazy Evaluation

These concepts are widely used in Cloud Platforms, SDKs, Automation Tools, and Enterprise Software.

---

# What is Abstraction?

Abstraction means hiding implementation details and showing only essential functionality.

Example:

Car

User knows:

- Accelerator
- Brake
- Steering

User does not know:

- Engine Timing
- Fuel Injection
- Internal Components

This is Abstraction.

---

# Why Abstraction?

Benefits:

- Reduced Complexity
- Better Security
- Professional Design
- Easy Maintenance
- Scalable Architecture

---

# Abstract Class

An Abstract Class acts as a blueprint.

It cannot be instantiated directly.

Example:

```python
from abc import ABC

class Vehicle(ABC):
    pass
```

Purpose:

Define rules that child classes must follow.

---

# Abstract Method

An Abstract Method has no implementation.

Example:

```python
from abc import abstractmethod

@abstractmethod
def start(self):
    pass
```

Every child class must implement it.

---

# ABC Module

Python provides:

```python
from abc import ABC
from abc import abstractmethod
```

Used to create:

- Abstract Classes
- Abstract Methods

---

# Interface Design

Python has no true interface.

Abstract Classes are used to create interface-like behavior.

Example:

Every Cloud Resource must implement:

- create()
- delete()
- monitor()

This ensures consistency.

---

# Iterators

Iterator produces one value at a time.

Functions:

```python
iter()
next()
```

Example:

```python
numbers = [10,20,30]

iterator = iter(numbers)

print(next(iterator))
```

Benefits:

- Memory Efficient
- Controlled Access

---

# Generators

Generators are special iterators.

Keyword:

```python
yield
```

Example:

```python
def numbers():

    yield 1

    yield 2

    yield 3
```

Benefits:

- Fast
- Memory Efficient
- Ideal For Large Data

---

# Cloud Engineering Use Cases

Abstract Classes:

- AWS SDK
- Azure SDK
- Terraform Resources

Generators:

- Log Processing
- Monitoring Systems
- Streaming Data
- Automation Pipelines

Iterators:

- API Responses
- Resource Lists
- Server Collections

---

# Mini Project

Cloud Backup Automation Simulator

Features:

- Abstract Classes
- Abstract Methods
- Polymorphism
- Cloud Backup Simulation

---

# Key Concepts Learned

- Abstraction
- Abstract Class
- Abstract Method
- ABC Module
- Interface Design
- Iterator
- Generator
- yield
- Lazy Evaluation

---

# Learning Outcome

By the end of Day 13, I can:

- Create Abstract Classes
- Use Abstract Methods
- Work with ABC Module
- Design Interface-Like Structures
- Create Iterators
- Create Generators
- Use yield Efficiently

---

## Author

Shubham Patil

36-Month Cloud Engineer Roadmap Journey

Day 13 - June 2026