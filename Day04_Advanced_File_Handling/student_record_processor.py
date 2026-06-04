import csv

file = open("students.csv", "r")

reader = csv.reader(file)

next(reader)

count = 0

print("Student Records")

for row in reader:
    print(row)
    count += 1

print("Total Students =", count)

file.close()