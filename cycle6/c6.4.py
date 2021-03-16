import csv
with open("D:/python/file/student.csv",newline="") as csvfile:
    data = csv.DictReader(csvfile)
    print("Name")
    for col in data:
        print(col['Name'])