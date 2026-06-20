import re

text = "Database Failed"

result = re.search(
    "Failed",
    text
)

if result:
    print("Match Found")
    print(result.group())
else:
    print("No Match")