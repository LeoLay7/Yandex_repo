import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, \
    QLCDNumber, QRadioButton, QListWidget


class MyWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 280, 300)
        self.bt = QPushButton('Загрузить текст', self)
        self.bt.move(10, 10)
        self.bt.clicked.connect(self.get_text)
        self.even = False
        self.l = QListWidget(self)
        self.l.move(10, 50)

    def get_text(self):
        self.l.clear()
        with open('lines.txt', mode='r', encoding='utf-8') as file:
            if self.even:
                text = file.readlines()[::2]
            else:
                text = file.readlines()[1::2]
            self.even = not self.even
            self.l.addItems([x.replace('\n', '') for x in text])


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec())
