class SeaMap:
    def __init__(self):
        self.field = [["." for _ in range(10)] for _ in range(10)]
        self.res = {"miss": "*", "hit": "x", "sink": "x"}

    def shoot(self, row, col, result):
        if result != "sink":
            self.field[row][col] = self.res[result]
        else:
            self.field[row][col] = "x"
            for i in range(col - 1, col - 5, - 1):  # корабль расположен горизонтально
                if 0 <= i <= 9:
                    if self.field[row][i] == "x":
                        if row < 9:
                            self.field[row + 1][i] = "*"
                        if row > 0:
                            self.field[row - 1][i] = "*"
                    else:
                        if row > 0:
                            self.field[row - 1][i] = "*"
                        self.field[row][i] = "*"
                        if row < 9:
                            self.field[row + 1][i] = "*"
                        break

            for i in range(col + 1, col + 5):
                if 0 <= i <= 9:
                    if self.field[row][i] == "x":
                        if row < 9:
                            self.field[row + 1][i] = "*"
                        if row > 0:
                            self.field[row - 1][i] = "*"
                    else:
                        if row > 0:
                            self.field[row - 1][i] = "*"
                        self.field[row][i] = "*"
                        if row < 9:
                            self.field[row + 1][i] = "*"
                        break

            for i in range(row - 1, row - 5, -1):  # вертикально
                if 0 <= i <= 9:
                    if self.field[i][col] == "x":
                        if col < 9:
                            self.field[i][col + 1] = "*"
                        if col > 0:
                            self.field[i][col - 1] = "*"
                    else:
                        if col < 9:
                            self.field[i][col + 1] = "*"
                        self.field[i][col] = "*"
                        if col > 0:
                            self.field[i][col - 1] = "*"
                        break

            for i in range(row + 1, row + 5):
                if 0 <= i <= 9:
                    if self.field[i][col] == "x":
                        if col < 9:
                            self.field[i][col + 1] = "*"
                        if col > 0:
                            self.field[i][col - 1] = "*"
                    else:
                        if col < 9:
                            self.field[i][col + 1] = "*"
                        self.field[i][col] = "*"
                        if col > 0:
                            self.field[i][col - 1] = "*"
                        break

    def cell(self, row, col):
        return self.field[row][col]

sm = SeaMap()

sm.shoot(0, 1, 'sink')
sm.shoot(2, 0, 'sink')
sm.shoot(0, 9, 'sink')
sm.shoot(9, 0, 'sink')

sm.shoot(4, 6, 'hit')
sm.shoot(4, 5, 'hit')
sm.shoot(4, 4, 'hit')
sm.shoot(4, 3, 'sink')

for row in range(10):
    for col in range(10):
        print(sm.cell(row, col), end='')
    print()



"""
0123456789
.......... 0
..xxx..... 1
.......... 2
...x...... 3
...x...... 4
...x...... 5
.......... 6 
.......... 7
.......... 8
.......... 9
"""

"""
sm.shoot(row, col, result) — добавить на карту результат выстрела, где
row — индекс ряда карты,
col — индекс вертикальной колонки карты,
result — одна из строк: “miss” (промах), “hit” (попадание), “sink” (потопление корабля).

sm.cell(row, col), который
возвращает ‘.’, если в клетке с координатами row, col может находиться корабль,
возвращает ‘*’, если в клетку уже стреляли или она находится рядом с потопленным кораблём,
возвращает ‘x’ если в клетке было попадание

Учтите, что не нужно помечать ‘*’ клетки рядом с кораблём, в который попали, но не потопили до конца.
"""