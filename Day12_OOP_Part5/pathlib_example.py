from pathlib import Path

print("Current Directory:")

print(Path.cwd())

print()

print("Home Directory:")

print(Path.home())

Path("logs").mkdir(exist_ok=True)

Path("report.txt").touch()

print()

print("Folder and file created successfully.")