import csv
mydict = {}
with open('School Data Labels.csv', 'r') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    for row in spamreader:
        mydict[row[0]] = row[1]

print(mydict)
