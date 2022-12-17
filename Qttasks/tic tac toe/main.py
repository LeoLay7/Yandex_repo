import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QLCDNumber, QRadioButton


class MyWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Крестики-нолики')
        self.radio1 = QRadioButton('x', self)
        self.radio1.move(85, 10)
        self.radio1.clicked.connect(lambda: self.main_sign_f('x'))

        self.radio2 = QRadioButton('o', self)
        self.radio2.move(125, 10)
        self.radio2.clicked.connect(lambda: self.main_sign_f('0'))

        self.sign = 'x'
        self.main_sign = 'x'

        self.buttons = [[QPushButton('', self), QPushButton('', self), QPushButton('', self)],
                        [QPushButton('', self), QPushButton('', self), QPushButton('', self)],
                        [QPushButton('', self), QPushButton('', self), QPushButton('', self)]]

        y = 50
        for i in range(3):
            x = 50
            for q in range(3):
                bt = self.buttons[i][q]
                bt.move(x, y)
                bt.resize(40, 40)
                bt.setEnabled(False)
                self.set_connect(bt, i, q)
                x += 50
            y += 50

        self.text = QLabel('Выиграл Х', self)
        self.text.hide()
        self.text.move(85, 30)

        self.start_bt = QPushButton('Начать', self)
        self.start_bt.move(85, 210)
        self.start_bt.clicked.connect(self.start)

    def set_value(self, a, b):
        def get_y(num):
            return self.buttons[0][num].text() + self.buttons[1][num].text() + self.buttons[2][num].text()

        self.buttons[a][b].setText(self.sign)
        if self.sign == 'x':
            self.sign = 'o'
        else:
            self.sign = 'x'

        field = self.get_values()

        if (field[1][1] == field[0][0] == field[2][2] or field[1][1] == field[0][2] == field[2][0]) \
                and field[1][1] != "":
            return self.end(field[1][1])

        for i in self.buttons:
            if ''.join([sign.text() for sign in i]) == 'xxx':
                return self.end('x')
            elif ''.join([sign.text() for sign in i]) == 'ooo':
                return self.end('o')

        for i in range(3):
            if get_y(i) == 'xxx':
                return self.end('x')
            elif get_y(i) == 'ooo':
                return self.end('o')

        if all([all([x.text() for x in i]) for i in self.buttons]):
            self.end('ничья')

    def set_connect(self, bt, a, b):
        bt.clicked.connect(lambda: self.set_value(a, b))

    def main_sign_f(self, val):
        self.main_sign = val

    def get_values(self):
        res = [[], [], []]
        for a in range(3):
            for b in range(3):
                res[a].append(self.buttons[a][b].text())
        return res

    def start(self):
        for i in self.buttons:
            for q in i:
                q.setText('')
                q.setEnabled(True)
        self.start_bt.setEnabled(False)
        self.sign = self.main_sign

    def end(self, winner):
        for i in self.buttons:
            for q in i:
                q.setEnabled(False)
        if winner == 'ничья':
            self.text.setText('Ничья')
        else:
            self.text.setText(f'Победитель: {winner}')
        self.text.show()
        self.start_bt.setEnabled(True)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec())
