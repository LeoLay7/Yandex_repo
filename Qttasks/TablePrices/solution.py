import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QTableWidget, QLabel, QTableWidgetItem
from PyQt5.QtCore import Qt


class Data:
    def get_input(self):
        res = []
        with open('prices.csv', encoding='utf-8') as file:
            lines = file.readlines()
            columns = lines[0].replace('\n', '').split(';')
            for i in lines[1:]:
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

        self.table.currentItemChanged.connect(self.current_item_changed)
        self.table.cellChanged.connect(self.cell_changed)

        self.current = None
        self.previous = None

    def cell_changed(self, row, column):
        curent_price = int(self.line.text()) + int(self.table.item(row, column - 1).text()) * \
                       (int(self.table.currentItem().text()) - int(self.current))

        self.line.setText(str(int(self.line.text()) + int(self.table.item(row, column - 1).text()) * \
                              (int(self.table.currentItem().text()) - int(self.current))))

    def current_item_changed(self, current, previous):
        # print(f'current = {current}, previous = {previous}')
        self.current = current.text() if current else ''
        self.previous = previous.text() if previous else ''


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec())
