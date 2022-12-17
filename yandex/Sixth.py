import csv


def get_input():
    res = []
    with open('exam.csv.csv', encoding='utf-8') as file:
        lines = file.readlines()
        columns = lines[0].replace('\n', '').split(';')
        for i in lines[1:]:
            product, price = i.replace('\n', '').split(';')
            res.append({})
            res[-1][columns[0]] = product
            res[-1][columns[1]] = price
    return res


def salarys(district, year1, year2):
    with open('exam.csv', mode='r', encoding='utf-8') as salary:
        lines = salary.readlines()
        res = []
        result = []
        columns = lines[0].replace('\n', '').split(';')
        for i in lines[1:]:
            stroka = i.replace('\n', '').split(';')
            res.append({})
            for q, item in enumerate(columns):
                res[-1][item] = stroka[q]
            need = int(res[-1][year1])
            # print(res[-1][year2], need + (need / 25), res[-1]['Федеральный округ'])
            if res[-1]['Федеральный округ'] == district and int(res[-1][year2]) < int(need + (need / 25)):
                result.append(f'{res[-1]["Субъект"]};{res[-1][year1]};{res[-1][year2]}')
        with open('out_file.csv', mode='w', encoding='utf-8') as output:
            if result:
                result.insert(0, f'Субъект;{year1};{year2}')
                output.write('\n'.join(result))
            else:
                output.write('')


if __name__ == '__main__':
    district = str(input())
    year1, year2 = input().split()
    salarys(district, year1, year2)
