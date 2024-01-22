# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/main.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CoffeeWindow(object):
    def setupUi(self, CoffeeWindow):
        CoffeeWindow.setObjectName("CoffeeWindow")
        CoffeeWindow.resize(600, 450)
        CoffeeWindow.setMinimumSize(QtCore.QSize(600, 450))
        CoffeeWindow.setMaximumSize(QtCore.QSize(600, 450))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        CoffeeWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(CoffeeWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(1, 10, 601, 441))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.addButton = QtWidgets.QPushButton(self.widget)
        self.addButton.setObjectName("addButton")
        self.horizontalLayout.addWidget(self.addButton)
        self.editButton = QtWidgets.QPushButton(self.widget)
        self.editButton.setObjectName("editButton")
        self.horizontalLayout.addWidget(self.editButton)
        self.deleteButton = QtWidgets.QPushButton(self.widget)
        self.deleteButton.setObjectName("deleteButton")
        self.horizontalLayout.addWidget(self.deleteButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tableWidget = QtWidgets.QTableWidget(self.widget)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.EditKeyPressed)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayout.addWidget(self.tableWidget)
        CoffeeWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(CoffeeWindow)
        QtCore.QMetaObject.connectSlotsByName(CoffeeWindow)

    def retranslateUi(self, CoffeeWindow):
        _translate = QtCore.QCoreApplication.translate
        CoffeeWindow.setWindowTitle(_translate("CoffeeWindow", "Латте макиато"))
        self.addButton.setText(_translate("CoffeeWindow", "Добавить"))
        self.editButton.setText(_translate("CoffeeWindow", "Изменить"))
        self.deleteButton.setText(_translate("CoffeeWindow", "Удалить"))
        self.deleteButton.setShortcut(_translate("CoffeeWindow", "Ctrl+S"))