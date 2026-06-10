class Student:

    def __init__(self):

        self.__age = 20

    def set_age(self, age):

        if age > 0:

            self.__age = age

    def get_age(self):

        return self.__age

s1 = Student()

s1.set_age(25)

print("Age:", s1.get_age())