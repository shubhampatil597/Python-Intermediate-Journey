from abc import ABC
from abc import abstractmethod


class CloudResource(ABC):

    @abstractmethod
    def create(self):

        pass

    @abstractmethod
    def delete(self):

        pass


class VirtualMachine(CloudResource):

    def create(self):

        print("VM Created")

    def delete(self):

        print("VM Deleted")


vm = VirtualMachine()

vm.create()

vm.delete()