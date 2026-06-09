class Student:

    college = "D Y Patil College"

    def __init__(self, name):
        self.name = name

s1 = Student("Shubham")
s2 = Student("Ram")

print("Student 1:", s1.name)
print("Student 2:", s2.name)

print("College:", Student.college)