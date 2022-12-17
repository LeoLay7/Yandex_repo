import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QLCDNumber, QRadioButton
import random


class MyWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 335, 50)
        self.bt = QPushButton('Получить', self)
        self.bt.move(10, 10)
        self.bt.clicked.connect(self.get_line)

        self.line = QLineEdit(self)
        self.line.move(100, 10)
        self.line.resize(200, 20)

    def get_line(self):

        file = open('lines.txt', mode='r', encoding='utf-8')
        if file:
            file_lines = file.readlines()
            if file_lines:
                self.line.setText(random.choice(file_lines))
        file.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec())
