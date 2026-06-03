#Program to Write Data into a File

file = open("sample.txt", "w")

file.write("Hello Python")
file.write("\nWelcome to File Handling")

file.close()

print("Data Written Successfully")