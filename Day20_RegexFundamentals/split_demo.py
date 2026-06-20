import re

text = "AWS,GCP,Azure"

result = re.split(
    ",",
    text
)

print(result)