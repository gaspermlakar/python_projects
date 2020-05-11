import csv

with open('10-01-CSV_file.csv') as data_file:
    reader = csv.DictReader(data_file)
    for row in reader:
        print(row['Name'], "is", row['Gender'], "and", row['Age'], "years old.")