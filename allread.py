import csv

filename = "film.csv"

fields = []
rows = []
 
with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    fields = next(csvreader)
    for row in csvreader:
        rows.append(row)
        print (row)

filename1 = "film2.csv"
with open(filename1, 'r') as csvfile:
    csvreader = csv.reader(csvfile) #pointer ??
    fields = next(csvreader)
    for row in csvreader:
        rows.append(row)
        print (row)

filename2 = 'allfilms.csv'
with open(filename2, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerows(rows)