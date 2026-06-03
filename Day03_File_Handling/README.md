Day 3 - File Handling

Aim

To study File Handling in Python.

---

Theory

What is a File?

A file is a collection of data stored permanently on a storage device.

Examples:

- notes.txt
- report.txt
- data.csv
- config.json

---

Why File Handling?

Variables store data temporarily.

Files store data permanently even after the program ends.

Applications:

- Student Records
- Banking Systems
- Log Files
- Configuration Files
- Monitoring Reports

---

open() Function

Used to open a file.

Syntax:

open(filename, mode)

Example:

file = open("sample.txt","r")

---

File Modes

Mode| Purpose
r| Read
w| Write
a| Append
x| Create

---

Reading a File

file = open("sample.txt","r")
print(file.read())
file.close()

---

Writing to a File

file = open("sample.txt","w")
file.write("Hello Python")
file.close()

---

Appending to a File

file = open("sample.txt","a")
file.write("\nCloud Engineering")
file.close()

---

FileNotFoundError

Occurs when the file does not exist.

Example:

open("abc.txt","r")

---

Relative Path

open("sample.txt")

Python searches in the current directory.

---

Absolute Path

open("/storage/emulated/0/Documents/sample.txt")

Full file location is specified.

---

Programs Performed

Program 1

Writing data to a file.

Program 2

Reading data from a file.

Program 3

Appending data to a file.

---

Applications

- Log Management
- Configuration Files
- Monitoring Reports
- Cloud Automation Scripts
- Backup Systems

---

Conclusion

Studied File Handling in Python including reading, writing, appending, file modes, and file paths.