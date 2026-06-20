import re

email = "cloudadmin@gmail.com"

result = re.search(
    r"(?P<username>\w+)@(?P<domain>\w+)\.(?P<extension>\w+)",
    email
)

print(
    result.group("username")
)

print(
    result.group("domain")
)

print(
    result.group("extension")
)