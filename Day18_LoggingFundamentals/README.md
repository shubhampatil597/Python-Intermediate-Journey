# Day 18 - Logging Fundamentals

## Topics Covered

### Logging Basics

- Why Logging Exists
- Logging vs print()
- logging Module

### Logging Levels

- DEBUG
- INFO
- WARNING
- ERROR
- CRITICAL

### Logging Configuration

- basicConfig()
- Log Formatting
- Timestamps

### File Logging

- Writing Logs to Files
- Persistent Logs

### Advanced Logging Basics

- Logger Objects
- Multiple Handlers
- Exception Logging
- Structured Logging

---

# What I Learned

## Logging

Logging records application events.

Used for:

- Monitoring
- Troubleshooting
- Auditing
- Security

---

## Logging Levels

### DEBUG

Developer Information

### INFO

Normal Events

### WARNING

Potential Problems

### ERROR

Operation Failed

### CRITICAL

Major Failure

---

## Log Formatting

Common Fields:

```python
%(asctime)s

%(levelname)s

%(message)s
```

---

## File Logging

Stores logs permanently.

Useful for:

- Incident Investigation
- Monitoring
- Compliance

---

## Logger Objects

Custom loggers help organize large applications.

Examples:

- API Logger
- Database Logger
- Authentication Logger

---

## Handlers

Control where logs are sent.

Examples:

- Console
- File
- Monitoring Systems

---

## Exception Logging

Captures:

- Error Messages
- Traceback
- Failure Details

---

## Structured Logging

Machine-readable logging.

Used by:

- AWS CloudWatch
- Azure Monitor
- Google Cloud Logging

---

# Mini Project

Cloud Monitoring Log Analyzer

Features:

- Log Analysis
- Error Detection
- Warning Detection
- File Logging
- Monitoring Simulation

---

# Learning Outcome

After Day 18 I can:

- Use Python Logging Module
- Configure Logging
- Use Log Levels
- Create Logger Objects
- Create File Logs
- Handle Exceptions Using Logs
- Understand Structured Logging
- Build Monitoring-Oriented Applications

---

Cloud Engineer Roadmap

June 2026

Author: Shubham Patil