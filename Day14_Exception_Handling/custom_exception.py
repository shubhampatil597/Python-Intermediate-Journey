class InvalidAgeError(Exception):

    pass


age = -10

if age < 0:

    raise InvalidAgeError(
        "Negative Age Not Allowed"
    )