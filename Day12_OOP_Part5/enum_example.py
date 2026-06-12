from enum import Enum


class Status(Enum):

    RUNNING = 1

    STOPPED = 2

    FAILED = 3


print(Status.RUNNING)

print(Status.STOPPED)

print(Status.FAILED)