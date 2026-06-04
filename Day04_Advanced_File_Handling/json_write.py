import json

student = {
    "name": "Shubham",
    "age": 20,
    "city": "Kolhapur"
}

file = open("student.json", "w")

json.dump(student, file)

file.close()

print("JSON File Created Successfully")