import csv

with open('task.csv', mode='r') as file:
    head = file.readline().replace('\n', '').split(',')
    print(head)
    reader = csv.DictReader(file, fieldnames=head, delimiter=',')

    res = []
    for i in reader:
        if i['is_manual'] == 'False' and int(i['max_points']) > 1:
            res.append([i['max_points']])

    for i in sorted(res, key=lambda x: x[0], reverse=True):
        print(*i)