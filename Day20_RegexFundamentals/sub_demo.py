import re

text = "Server IP 192.168.1.10"

result = re.sub(
    r"\d",
    "X",
    text
)

print(result)