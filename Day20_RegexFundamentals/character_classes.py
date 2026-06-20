import re

text = "Server101"

digit = re.search(
    r"\d",
    text
)

letter = re.search(
    r"[a-zA-Z]",
    text
)

print("Digit:", digit.group())
print("Letter:", letter.group())