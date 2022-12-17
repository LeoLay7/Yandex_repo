import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout
from layout import Ui_Form


class MyWidget(QWidget, Ui_Form):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setupUi(self)
        self.pushButton.clicked.connect(self.add_to_sp)


    def add_to_sp(self):
        self.listWidget.addItem(f'{self.lineEdit.text()} {self.lineEdit_2.text()}')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec())
