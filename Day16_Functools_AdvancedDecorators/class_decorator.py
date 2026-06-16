def register(cls):

    print(

        f"Registering Class: {cls.__name__}"

    )

    return cls


@register
class Server:

    pass


server = Server()