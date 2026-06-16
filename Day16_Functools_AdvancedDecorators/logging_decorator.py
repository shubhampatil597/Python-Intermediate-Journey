from functools import wraps


def logger(func):

    @wraps(func)

    def wrapper(*args, **kwargs):

        print(

            f"Running Function: {func.__name__}"

        )

        return func(

            *args,

            **kwargs

        )

    return wrapper


@logger
def deploy():

    print("Deployment Started")


deploy()