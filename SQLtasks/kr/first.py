import csv

ships = str(input()).split(', ')


with open('sailors.csv', mode='r') as file:
    head = file.readline().replace('\n', '').split(';')

    reader = csv.DictReader(file, delimiter=';', fieldnames=head)

    res = []

    for i in reader:
        if (i['ship'] in ships or i['occupation'] == 'pirate') and 40 <= int(i['age']) <= 60:
            res.append(i['name'])

    for i in sorted(res):
        print(i)