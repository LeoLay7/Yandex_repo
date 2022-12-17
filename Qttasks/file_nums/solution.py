import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QLCDNumber, QRadioButton
import random
from nums import Ui_Form


class MyWidget(QWidget, Ui_Form):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setupUi(self)
        self.bt.clicked.connect(self.calculate)

        self.errorlabel.resize(300, 20)
        self.errorlabel.hide()

    def calculate(self):
        try:
            filename = self.fileline.text()
            file = open(filename, mode='r', encoding='utf-8')

            text = [int(x) for x in file.read().replace('\t', ' ').replace('\n', ' ').split()]

            self.maxline.setText(str(max(text)))
            self.minline.setText(str(min(text)))
            self.averageline.setText(str(round(sum(text) / len(text), 3)))

            if not self.errorlabel.isHidden():
                self.errorlabel.hide()

        # except Exception as error:
        #     print('Произошла ошибка:', error.__class__.__name__, error)
        #     вопрос, а можно делать так, если боишься пропустить
        #     ошибку, из-за которой можнет упасть прога? Но только в более
        #     больших проектах информацию об ошибках в базу данных скидывать или тому подобное

        except FileNotFoundError:
            self.errorlabel.show()
            self.errorlabel.setText('Файл отсутствует')
        except ValueError:
            self.errorlabel.show()
            self.errorlabel.setText('Файл содержит неверный формат данных')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec())
