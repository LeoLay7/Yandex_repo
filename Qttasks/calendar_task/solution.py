import sys
from PyQt5.QtWidgets import QApplication, QWidget
from calendar import Ui_Form


class MyWidget(QWidget, Ui_Form):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setupUi(self)
        self.ivents = []

        self.pushButton.clicked.connect(self.add_ivent)

    def add_ivent(self):
        date = f'{self.calendarWidget.selectedDate().year():02}-' \
               f'{self.calendarWidget.selectedDate().month():02}-' \
                f'{self.calendarWidget.selectedDate().day():02}'

        time = f'{self.timeEdit.time().hour():02}:{self.timeEdit.time().minute():02}:' \
               f'{self.timeEdit.time().second():02}'
        ivent = self.lineEdit.text()
        self.ivents.append(f'{date} {time} - {ivent}')
        self.listWidget.clear()
        self.listWidget.addItems(sorted(self.ivents, key=lambda x: self.sort_date(x)))

    def sort_date(self, date: str):
        a = date.split(' - ')
        date = a[0].split(' ')[0].split('-')
        time = a[0].split(' ')[1].split(':')
        return tuple(date + time)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec())
