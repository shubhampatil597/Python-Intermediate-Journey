import time

from functools import wraps


def logger(func):

    @wraps(func)

    def wrapper(*args, **kwargs):

        print("Logger Started")

        return func(

            *args,

            **kwargs

        )

    return wrapper


def timer(func):

    @wraps(func)

    def wrapper(*args, **kwargs):

        start = time.time()

        result = func(

            *args,

            **kwargs

        )

        end = time.time()

        print(

            f"Time: {end-start:.2f}"

        )

        return result

    return wrapper


@logger
@timer
def deploy():

    time.sleep(1)

    print("Deploying Application")


deploy()