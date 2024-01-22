import sys
import sqlite3

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QHeaderView


class Espresso(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)

        self.fill_data()

    def fill_data(self):
        connection = sqlite3.connect('coffee.sqlite')
        data = connection.cursor().execute('SELECT * FROM coffee').fetchall()
        connection.close()

        self.headers = ('ID', 'Название', 'Прожарка', 'Тип', 'Описание', 'Цена (₽)', 'Объем (мл)')
        self.tableWidget.setColumnCount(len(self.headers))
        self.tableWidget.setRowCount(len(data))
        self.tableWidget.setHorizontalHeaderLabels(self.headers)
        for i, row in enumerate(data):
            for j, elem in enumerate(row):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(elem)))
        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.horizontalHeader().setSectionResizeMode(4, QHeaderView.Stretch)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Espresso()
    ex.show()
    sys.exit(app.exec())
