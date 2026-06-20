import re

email = "admin@gmail.com"

result = re.search(
    r"(\w+)@(\w+)\.(\w+)",
    email
)

print("Username:", result.group(1))
print("Domain:", result.group(2))
print("Extension:", result.group(3))