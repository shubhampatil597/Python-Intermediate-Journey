import csv

file = open("students.csv", "w", newline="")

writer = csv.writer(file)

writer.writerow(["Name", "Age", "City"])
writer.writerow(["Shubham", 20, "Kolhapur"])
writer.writerow(["Rahul", 21, "Pune"])
writer.writerow(["Priya", 22, "Mumbai"])

file.close()

print("CSV File Created Successfully")