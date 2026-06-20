import re

text = "Port 8080 Error 404 Server 101"

numbers = re.findall(
    r"\d+",
    text
)

print(numbers)