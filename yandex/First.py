x1, y1, width1, heigth1 = [int(x) for x in input().split()]
x2, y2, width2, heigth2 = [int(x) for x in input().split()]

intersection = False

if (x1 <= x2 <= x1 + width1 or x2 <= x1 <= x2 + width2) and (y1 <= y2 <= y1 + heigth1 or y2 <= y1 <= y2 + heigth2):
    intersection = True

if intersection:
    print('YES')
else:
    print('NO')
