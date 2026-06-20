import re

mobile = input(
    "Enter Mobile Number: "
)

pattern = r"\d{10}"

if re.fullmatch(
    pattern,
    mobile
):
    print("Valid Mobile Number")
else:
    print("Invalid Mobile Number")