# Day 14 - Exception Handling Mastery & Professional Python

## Topics Covered

### Core Python

- Exceptions
- Syntax Errors vs Exceptions
- try
- except
- else
- finally
- Multiple Exceptions
- Exception Hierarchy
- raise
- Custom Exceptions

### Professional Python

- Context Managers
- with Statement
- Decorator Introduction

---

# What is an Exception?

An Exception is an error that occurs while a program is running.

Example:

```python
print(10 / 0)
```

Output:

```text
ZeroDivisionError
```

Without exception handling the program crashes.

---

# Why Exception Handling?

Benefits:

- Prevent Program Crashes
- Improve Reliability
- Better User Experience
- Professional Error Management

---

# try Block

Used to monitor risky code.

Example:

```python
try:

    print(10 / 0)
```

---

# except Block

Handles exceptions.

Example:

```python
except ZeroDivisionError:

    print("Cannot Divide By Zero")
```

---

# else Block

Runs only when no exception occurs.

Example:

```python
else:

    print("Success")
```

---

# finally Block

Runs regardless of success or failure.

Used for:

- Closing Files
- Closing Database Connections
- Releasing Resources

---

# Exception Hierarchy

BaseException

└── Exception

     ├── ValueError

     ├── TypeError

     ├── ZeroDivisionError

     ├── IndexError

     ├── KeyError

     └── FileNotFoundError

---

# Raising Exceptions

Python allows manual creation of exceptions.

Example:

```python
raise ValueError(
    "Invalid Age"
)
```

---

# Custom Exceptions

Create your own exceptions.

Example:

```python
class InvalidAgeError(Exception):

    pass
```

Benefits:

- Better Debugging
- Better Error Messages
- Cleaner Code

---

# Context Managers

Manage resources automatically.

Example:

```python
with open(
    "file.txt"
) as file:

    data = file.read()
```

Python automatically closes the file.

---

# Decorators

A decorator modifies another function without changing its original code.

Common Uses:

- Logging
- Authentication
- Monitoring
- Validation

Frameworks Using Decorators:

- Flask
- FastAPI
- Django

---

# Mini Project

Cloud Log Analyzer

Features:

- File Handling
- Exception Handling
- Context Managers
- Error Recovery

---

# Key Concepts Learned

- Exceptions
- try
- except
- else
- finally
- raise
- Custom Exceptions
- Context Managers
- with Statement
- Decorators

---

# Learning Outcome

After Day 14 I can:

- Handle Runtime Errors
- Create Custom Exceptions
- Use Context Managers
- Use with Statement
- Understand Decorator Fundamentals
- Build Reliable Python Programs

---

Cloud Engineer Roadmap

Day 14 - June 2026

Author: Shubham Patil