from dataclasses import dataclass

@dataclass
class Student:
    name: str
    age: int

student1 = Student("Shubham", 20)

print(student1)