import csv

f = open('prasarana.csv','r')
reader = csv.reader(f)

for row in reader:
    print(row)

f.close()    