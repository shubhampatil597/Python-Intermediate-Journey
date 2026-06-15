def logger(func):

    def wrapper(**kwargs):

        print(kwargs)

        return func(**kwargs)

    return wrapper


@logger
def profile(name):

    print(name)


profile(name="Shubham")