from functools import wraps


def decorator(func):

    @wraps(func)

    def wrapper():

        print("Decorator Running")

        func()

    return wrapper


@decorator
def greet():

    """Greeting Function"""

    print("Hello Cloud Engineer")


greet()

print("Function Name:", greet.__name__)

print("Doc String:", greet.__doc__)