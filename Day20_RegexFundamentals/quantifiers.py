import re

text = "abbb"

result = re.search(
    r"ab+",
    text
)

print(result.group())