from abc import ABC
from abc import abstractmethod


class Employee(ABC):

    @abstractmethod
    def work(self):

        pass


class Developer(Employee):

    def work(self):

        print("Writing Python Code")


dev = Developer()

dev.work()