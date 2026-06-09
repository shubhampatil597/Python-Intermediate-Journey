class Student:

    college = "D Y Patil College"

    @classmethod
    def show_college(cls):
        print("College Name:", cls.college)

Student.show_college()