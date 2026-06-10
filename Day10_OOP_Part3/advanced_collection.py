from collections import namedtuple
from collections import OrderedDict
from collections import ChainMap

print("NAMEDTUPLE")

Student = namedtuple(
    "Student",
    ["name", "age"]
)

s1 = Student(
    "Shubham",
    20
)

print(s1.name)
print(s1.age)

print("\nORDEREDDICT")

data = OrderedDict()

data["Name"] = "Shubham"
data["Course"] = "Python"
data["City"] = "Pune"

print(data)

print("\nCHAINMAP")

dict1 = {
    "name": "Shubham"
}

dict2 = {
    "city": "Pune"
}

result = ChainMap(
    dict1,
    dict2
)

print(result["name"])
print(result["city"])