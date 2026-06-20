import re

text = "Cloud"

result = re.fullmatch(
    "Cloud",
    text
)

if result:
    print("Full Match Found")
else:
    print("No Full Match")