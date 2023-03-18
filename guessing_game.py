import csv

#download data from flat files
def reader(filename):
    with open(filename, encoding = 'utf-8') as file:
        r = csv.DictReader(file)
        return list(r)

quotes = reader("quotes.csv")
bio = reader("bio.csv")