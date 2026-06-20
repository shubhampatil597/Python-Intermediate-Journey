import re

text = "Error 404 Error 500"

matches = re.finditer(
    r"Error",
    text
)

for match in matches:
    print(
        "Found at position:",
        match.start()
    )