import re

logs = """
INFO Server Started
ERROR Database Failed
INFO Request Received
WARNING CPU High
ERROR Timeout
"""

errors = re.findall(
    r"ERROR.*",
    logs
)

print("Errors Found:")

for error in errors:
    print(error)