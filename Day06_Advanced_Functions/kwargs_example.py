# Using **kwargs

def student(**details):

    for key, value in details.items():
        print(key, ":", value)

student(
    name="Shubham",
    age=20,
    city="Kolhapur"
)