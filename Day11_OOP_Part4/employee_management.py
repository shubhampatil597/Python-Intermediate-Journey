class Employee:

    def __init__(self, name, salary):

        self.name = name
        self.salary = salary

    def job_role(self):

        print("Employee")


class Developer(Employee):

    def __init__(self, name, salary):

        super().__init__(name, salary)

    def job_role(self):

        print("Developer")


class Tester(Employee):

    def __init__(self, name, salary):

        super().__init__(name, salary)

    def job_role(self):

        print("Tester")


dev = Developer(
    "Shubham",
    50000
)

tester = Tester(
    "Amit",
    40000
)

print(dev.name)
dev.job_role()

print(tester.name)
tester.job_role()