import re

logs = """
Login Success
Failed Login
Failed Login
Unauthorized Access
Login Success
"""

suspicious = re.findall(
    r"Failed Login|Unauthorized Access",
    logs
)

print(
    "Suspicious Activities:"
)

for item in suspicious:
    print(item)