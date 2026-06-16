# Day 16 - functools & Advanced Decorators

## Topics Covered

### functools Module

- functools Introduction
- Higher Order Functions
- Function Utilities

### partial()

- Function Preconfiguration
- Reusable Functions

### wraps()

- Metadata Preservation
- Production Decorator Design

### lru_cache()

- Caching
- Performance Optimization
- Memoization

### Class Decorators

- Decorating Classes
- Registration Pattern

### Advanced Decorators

- Logging Decorators
- Timing Decorators
- Decorator Chaining

---

# What I Learned

## partial()

Creates specialized versions of existing functions.

Example:

```python
double = partial(multiply, 2)
```

---

## wraps()

Preserves:

- Function Name
- Documentation
- Metadata

Used in professional decorators.

---

## lru_cache()

Caches previous function results.

Benefits:

- Faster Execution
- Less CPU Usage
- Better Performance

---

## Memoization

Store previous calculations.

Avoid repeating expensive operations.

---

## Class Decorators

Decorate classes instead of functions.

Useful for:

- Registration
- Validation
- Framework Internals

---

## Logging Decorators

Track:

- Function Calls
- User Actions
- API Requests

---

## Timing Decorators

Measure:

- Performance
- Execution Time
- Optimization Opportunities

---

# Mini Project

Cloud API Request Tracker

Features:

- Logging
- Timing
- Decorator Chaining
- API Monitoring

---

# Learning Outcome

After Day 16 I can:

- Use functools
- Create partial functions
- Use wraps()
- Implement caching with lru_cache()
- Understand memoization
- Create class decorators
- Build logging decorators
- Build timing decorators
- Chain decorators together
- Create monitoring utilities

---

Cloud Engineer Roadmap

June 2026

Author: Shubham Patil