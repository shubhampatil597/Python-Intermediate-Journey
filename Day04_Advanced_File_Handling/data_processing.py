import csv

file = open("marks.csv", "r")

reader = csv.reader(file)

next(reader)

total = 0

for row in reader:
    total += int(row[1])

print("Total Marks =", total)

file.close()