from PyQt5 import uic
from PyQt5.QtWidgets import QWidget
from add_edit_form import Ui_CoffeeRecord

fields = ['name', 'roast', 'type', 'taste', 'price', 'volume']


class Add_edit_form(QWidget, Ui_CoffeeRecord):
    def __init__(self, parent):
        super().__init__()
        self.setupUi(self)
        self.parent = parent
        self.id = None
        self.okButton.clicked.connect(self.save)
        self.cancelButton.clicked.connect(self.close)

    def fill(self, data):
        self.id = data[0]
        for i, n in enumerate(fields):
            self.__getattribute__(f'lineEdit_{n}').setText(str(data[i + 1]))

    def closeEvent(self, event):
        self.id = None
        for n in fields:
            self.__getattribute__(f'lineEdit_{n}').setText('')
        self.parent.show()

    def save(self):
        res = [''] * self.parent.fields_cnt
        res[0] = self.id
        for i, n in enumerate(fields):
            res[i + 1] = self.__getattribute__(f'lineEdit_{n}').text()
        self.parent.update_data(res)
        self.close()
