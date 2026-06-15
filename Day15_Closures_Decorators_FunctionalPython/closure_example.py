def outer():

    message = "Hello"

    def inner():

        print(message)

    return inner


func = outer()

func()