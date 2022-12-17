import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, \
    QLineEdit, QPushButton, QLCDNumber, QCheckBox, QRadioButton, QPlainTextEdit
from flag import Ui_Dialog


class MyWidget(QWidget, Ui_Dialog):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setupUi(self)
        self.flag = ['Cиний', 'Синий', 'Синий']
        self.radioButton.clicked.connect(lambda: self.colors('Зеленый', 0))
        self.radioButton_2.clicked.connect(lambda: self.colors('Синий', 0))
        self.radioButton_3.clicked.connect(lambda: self.colors('Красный', 0))
        self.radioButton_2.setChecked(True)

        self.radioButton_4.clicked.connect(lambda: self.colors('Зеленый', 1))
        self.radioButton_5.clicked.connect(lambda: self.colors('Синий', 1))
        self.radioButton_6.clicked.connect(lambda: self.colors("Красный", 1))
        self.radioButton_5.setChecked(True)

        self.radioButton_7.clicked.connect(lambda: self.colors('Зеленый', 2))
        self.radioButton_8.clicked.connect(lambda: self.colors('Красный', 2))
        self.radioButton_9.clicked.connect(lambda: self.colors('Синий', 2))
        self.radioButton_9.setChecked(True)

        self.pushButton.clicked.connect(self.get_flag)

        self.label_4.hide()

    def colors(self, color, pos):
        self.flag[pos] = color

    def get_flag(self):
        self.label_4.setText(f'Цвета: {", ".join(self.flag)}')
        self.label_4.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec())