x1, y1, r1 = [int(x) for x in input().split()]
x2, y2, r3 = [int(x) for x in input().split()]

if x1 == x2:
    S = abs(y1 - y2)
elif y1 == y2:
    S = abs(x1 - x2)
else:
    S = ((x1 - x2) ** 2 + (y1 - y1) ** 2) ** 0.5

if S <= r1 + r3:
    print('YES')
else:
    print('NO')