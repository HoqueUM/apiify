import csv

pops = []
with open('websites.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        pops.append(row[1].strip())
print(pops)