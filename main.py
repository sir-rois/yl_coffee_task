import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QHeaderView

from add_edit import Add_edit_form
from data import Data
from main_form import Ui_CoffeeWindow


class Coffee(QMainWindow, Ui_CoffeeWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.add_edit_form = Add_edit_form(self)
        self.fields_cnt = 7
        self.stretch_idx = 4

        self.data = Data()
        self.fill_data()
        self.addButton.clicked.connect(self.add_coffee)
        self.editButton.clicked.connect(self.edit_coffee)
        self.deleteButton.clicked.connect(self.delete_coffee)

    def fill_data(self):
        self.headers = ('ID', 'Название', 'Прожарка', 'Тип', 'Описание', 'Цена (Р)', 'Объем (мл)')
        self.tableWidget.setColumnCount(self.fields_cnt)
        self.tableWidget.setRowCount(len(self.data))
        self.tableWidget.setHorizontalHeaderLabels(self.headers)
        for i, row in enumerate(self.data):
            for j, elem in enumerate(row):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(elem)))
        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.horizontalHeader().setSectionResizeMode(self.stretch_idx, QHeaderView.Stretch)
        if len(self.data) > 0:
            self.tableWidget.selectRow(0)

    def add_coffee(self):
        self.hide()
        self.add_edit_form.show()

    def edit_coffee(self):
        if self.tableWidget.currentRow() == -1:
            return
        self.add_edit_form.fill(self.data[int(self.tableWidget.item(self.tableWidget.currentRow(), 0).text())])
        self.hide()
        self.add_edit_form.show()

    def delete_coffee(self):
        if self.tableWidget.currentRow() == -1:
            return
        id = int(self.tableWidget.item(self.tableWidget.currentRow(), 0).text())
        self.data.delete(id)
        self.fill_data()

    def update_data(self, data):
        if data[0] is None:
            self.data.create(data[1:])
        else:
            self.data.update(data[0], data[1:])
        self.fill_data()

    def closeEvent(self, event):
        del self.data


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Coffee()
    ex.show()
    sys.exit(app.exec())
