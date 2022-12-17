with open('pipes.txt', mode='r', encoding='utf-8') as file:
    if file:
        lines = [x.replace('\n', '').lstrip() for x in file.readlines()]
        print(lines)
        pipes = lines[:lines.index('')]
        use_pipes = [pipes[int(x) - 1] for x in lines[-1].split()]
        print('PIPES', pipes, use_pipes)
        with open('time.txt', mode='w', encoding='utf-8') as res:
            res.write(str(1 / sum([1 / (60 * float(i)) for i in use_pipes])))
