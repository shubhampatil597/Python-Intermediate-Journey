import re

text = "Cloud Engineer"

result = re.match(
    "Cloud",
    text
)

if result:
    print("Match Found")
    print(result.group())
else:
    print("No Match")