import re

text = "cloud engineer"

result = re.search(
    "CLOUD",
    text,
    re.IGNORECASE
)

if result:
    print("Match Found")
else:
    print("No Match")