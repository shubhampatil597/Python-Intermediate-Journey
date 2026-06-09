class Student:

    @staticmethod
    def is_adult(age):
        return age >= 18

print(Student.is_adult(20))
print(Student.is_adult(15))