class Student:

    def __init__(self):

        self.__age = 20

    def get_age(self):

        return self.__age

s1 = Student()

print("Age:", s1.get_age())