import sys
from PyQt5.QtWidgets import QApplication, QWidget
from calc import Ui_Form
from math import factorial
import difflib

class MyWidget(QWidget, Ui_Form):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setupUi(self)

        self.sign = ''
        self.num = '0'
        self.res_num = 0

        self.btn0.clicked.connect(lambda: self.add_lcdvalue(str(0)))
        self.btn1.clicked.connect(lambda: self.add_lcdvalue(str(1)))
        self.btn2.clicked.connect(lambda: self.add_lcdvalue(str(2)))
        self.btn3.clicked.connect(lambda: self.add_lcdvalue(str(3)))
        self.btn4.clicked.connect(lambda: self.add_lcdvalue(str(4)))
        self.btn5.clicked.connect(lambda: self.add_lcdvalue(str(5)))
        self.btn6.clicked.connect(lambda: self.add_lcdvalue(str(6)))
        self.btn7.clicked.connect(lambda: self.add_lcdvalue(str(7)))
        self.btn8.clicked.connect(lambda: self.add_lcdvalue(str(8)))
        self.btn9.clicked.connect(lambda: self.add_lcdvalue(str(9)))

        self.btn_plus.clicked.connect(lambda: self.plus())
        self.btn_minus.clicked.connect(lambda: self.minus())
        self.btn_mult.clicked.connect(lambda: self.mult())
        self.btn_div.clicked.connect(lambda: self.div())
        self.btn_clear.clicked.connect(lambda: self.clear())
        self.btn_fact.clicked.connect(self.fact)
        self.btn_sqrt.clicked.connect(lambda: self.sqrt())
        self.btn_pow.clicked.connect(lambda: self.pow())

        self.btn_eq.clicked.connect(self.equal)
        self.btn_dot.clicked.connect(lambda: self.dot())

    def add_lcdvalue(self, val):
        self.num += val
        if self.num[0] == '0' and val != '0':
            self.num = self.num[1:]
        if float(self.num) % 1 > 0:
            self.table.display(float(self.num))
        else:
            self.table.display(int(self.num))

    def fact(self):
        if self.num:
            self.res_num = float(self.num)  # LCD num не выводит факториал при num > 8, я хз как это фиксить :(
        if self.res_num >= 0:
            self.res_num = factorial(int(self.res_num))
        else:
            self.table.display('Error')
        # print('Факториал равен:', self.res_num)
        self.table.display(self.res_num)
        self.num = ''

    def pow(self):
        if self.num:
            self.res_num = float(self.num)
        self.sign = '**'
        self.num = ''

    def dot(self):
        self.num += '.'
        a = self.num[:self.num.index('.')]
        if a.count('0') > 1:
            self.num = self.num[len(a) - 1:]
        self.table.display(self.num)

    def plus(self):
        if self.num:
            self.res_num = float(self.num)
        self.sign = '+'
        self.num = ''

    def minus(self):
        if self.num and self.num != '0':
            self.res_num = float(self.num)
            self.sign = '-'
            self.num = ''
        else:
            if self.sign or self.num == '0':
                self.num = '-'
                self.table.display(self.num)
            else:
                self.sign = '-'

    def mult(self):
        if self.num:
            self.res_num = float(self.num)
        self.sign = '*'
        self.num = ''

    def div(self):
        if self.num:
            self.res_num = float(self.num)
        self.sign = '/'
        self.num = ''

    def clear(self):
        self.sign = ''
        self.num = '0'
        self.res_num = 0
        self.table.display(0)

    def sqrt(self):
        if self.num:
            if float(self.num) >= 0:
                self.res_num = float(self.num) ** 0.5
                self.table.display(self.res_num)
            else:
                self.table.display('Error')
        else:
            if self.res_num >= 0:
                self.res_num **= 0.5
                self.table.display(self.res_num)
            else:
                self.table.display('Error')
        self.num = ''

    def equal(self):
        is_error = False
        num = float(self.num)
        if self.sign == '+':
            self.res_num += num

        elif self.sign == '-':
            self.res_num -= num

        elif self.sign == '*':
            self.res_num *= num

        elif self.sign == '/':
            if num != 0:
                self.res_num /= num
            else:
                is_error = True
                self.table.display('Error')

        elif self.sign == '**':
            if self.num:
                self.res_num = float(self.res_num) ** num
            else:
                self.res_num = float(self.res_num) ** self.res_num
        self.num = ''
        self.sign = ''
        if not is_error:
            if self.res_num % 1 > 0:
                self.table.display(float(self.res_num))
            else:
                self.table.display(int(self.res_num))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec())
