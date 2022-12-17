import csv


def multi_data(data):
    res = []
    for j in data.split(';'):
        if j in process and process[j]:
            res.append(int(process[j]))
            # print(res)
        else:
            return None
    return max(res)


def steck(data):
    if data in process and process[data]:
        return process[data]
    # print(data, datas[data])
    try:
        return max([steck(x) for x in datas[data]])
    except KeyError:
        return ''


with open('aaa.csv', mode='r', encoding='windows-1251') as file:
    headings = file.readline().replace('\n', '').split(';')
    reader = csv.DictReader(file, fieldnames=headings, delimiter=';')

    process = {'1': ''}
    datas = {'1': ['0']}
    # while not all([process[x] for x in process]):
    for i in range(15):
        for i in reader:
            id = i['id']
            data: str = i['data']
            time = i['time']

            if id not in process:
                process[id] = ''
                datas[id] = data.split(';')
            if data == '0':
                process[id] = time
            elif data.count(';') == 0:
                if data in process and process[data]:
                    process[id] = process[data]
            elif data.count(';') > 0:
                process[id] = steck(id)

print([datas[x] for x in process.keys() if not process[x]])

print(process)