import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QTableWidget, QLabel, QTableWidgetItem, QPushButton
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor
from random import choices


class Data:
    def get_input(self):
        res = []
        with open('prices.txt', encoding='utf-8') as file:
            lines = file.readlines()
            columns = lines[0].replace('\n', '').split(';')
            for i in sorted(lines[1:], key=lambda x: int(x.replace('\n', '').split(';')[1]))[::-1]:
                product, price = i.replace('\n', '').split(';')
                res.append({})
                res[-1][columns[0]] = product
                res[-1][columns[1]] = price
                res[-1]['Количество'] = 0
        return res


class MyWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.data = Data()
        self.bindData()

    def initUI(self):
        self.setGeometry(300, 300, 420, 300)
        self.table = QTableWidget(self)
        self.table.resize(400, 250)
        self.table.move(10, 10)
        self.table.verticalHeader().setDefaultSectionSize(40)

        self.line = QLineEdit(self)
        self.line.move(200, 270)
        self.line.resize(190, 20)
        self.line.setText('0')
        self.line.setEnabled(False)

        self.label = QLabel('Итого:', self)
        self.label.move(160, 270)

        self.bt = QPushButton('Обновить', self)
        self.bt.move(10, 270)
        self.bt.clicked.connect(self.change_color)

    def bindData(self):
        columns = self.data.get_input()[0].keys()
        self.table.setColumnCount(len(columns))
        self.table.setHorizontalHeaderLabels(columns)
        self.table.setRowCount(len(self.data.get_input()))

        for i, item in enumerate(self.data.get_input()):
            for j, value in enumerate(item.values()):
                item = QTableWidgetItem(str(value))
                if j != 2:
                    item.setFlags(Qt.ItemIsEnabled)
                self.table.setItem(i, j, item)

        self.change_color()

    def random_color(self):
        symbs = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
        return f'#{"".join(choices(symbs, k=6))}'

    def change_color(self):
        for i in range(5):
            color = self.random_color()
            for q in range(3):
                self.table.item(i, q).setBackground(QColor(color))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec())
