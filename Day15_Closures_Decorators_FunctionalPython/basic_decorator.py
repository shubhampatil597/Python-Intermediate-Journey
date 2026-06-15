def decorator(func):

    def wrapper():

        print("Starting")

        func()

        print("Finished")

    return wrapper


@decorator
def greet():

    print("Hello")


greet()