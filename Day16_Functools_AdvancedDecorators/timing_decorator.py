import time

from functools import wraps


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

            f"Execution Time: {end-start:.2f} seconds"

        )

        return result

    return wrapper


@timer
def process():

    time.sleep(2)

    print("Processing...")


process()