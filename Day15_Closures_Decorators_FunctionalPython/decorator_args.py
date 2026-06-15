def logger(func):

    def wrapper(*args):

        print("Arguments:", args)

        return func(*args)

    return wrapper


@logger
def add(a, b):

    return a + b


print(add(10, 20))