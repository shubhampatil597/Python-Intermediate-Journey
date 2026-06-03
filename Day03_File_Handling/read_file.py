#Program to Read Data from a File

file = open("sample.txt", "r")

data = file.read()

print(data)

file.close()