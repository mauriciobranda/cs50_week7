import csv

titles = set()

with open("favorites.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        title = row["title"].strip().upper()
        #if not title in titles: #se o registro ja estier na lista, não adiciona
        titles.add(title)


for title in sorted(titles):        
    print(title)