import csv

with open('10-01-CSV_file.csv') as data_file:
    people_list = csv.DictReader(data_file)
    for people_info in people_list:
        print(people_info['Name'], "is", people_info['Gender'], "and", people_info['Age'], "years old.")