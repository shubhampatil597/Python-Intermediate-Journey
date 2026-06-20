import re

text = "Cloud Engineer"

start = re.search(
    r"^Cloud",
    text
)

end = re.search(
    r"Engineer$",
    text
)

print("Start Match:", bool(start))
print("End Match:", bool(end))