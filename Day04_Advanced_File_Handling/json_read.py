import json

file = open("student.json", "r")

data = json.load(file)

print("Name:", data["name"])
print("Age:", data["age"])
print("City:", data["city"])

file.close()