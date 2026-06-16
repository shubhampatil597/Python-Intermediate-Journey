import time

from functools import wraps


def logger(func):

    @wraps(func)

    def wrapper(*args, **kwargs):

        print(

            f"Request Started: {func.__name__}"

        )

        result = func(

            *args,

            **kwargs

        )

        print(

            f"Request Finished: {func.__name__}"

        )

        return result

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

            f"Execution Time: {end-start:.2f} sec"

        )

        return result

    return wrapper


@logger
@timer
def api_request():

    time.sleep(2)

    print("Calling Cloud API...")


api_request()