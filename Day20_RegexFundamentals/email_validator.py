import re

email = input(
    "Enter Email: "
)

pattern = r"\w+@\w+\.\w+"

if re.fullmatch(
    pattern,
    email
):
    print("Valid Email")
else:
    print("Invalid Email")