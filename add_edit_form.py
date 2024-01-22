# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/addEditCoffeeForm.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CoffeeRecord(object):
    def setupUi(self, CoffeeRecord):
        CoffeeRecord.setObjectName("CoffeeRecord")
        CoffeeRecord.resize(252, 273)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        CoffeeRecord.setFont(font)
        self.widget = QtWidgets.QWidget(CoffeeRecord)
        self.widget.setGeometry(QtCore.QRect(0, 0, 251, 251))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_name = QtWidgets.QLabel(self.widget)
        self.label_name.setObjectName("label_name")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_name)
        self.lineEdit_name = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_name)
        self.label_roast = QtWidgets.QLabel(self.widget)
        self.label_roast.setObjectName("label_roast")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_roast)
        self.lineEdit_roast = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_roast.setObjectName("lineEdit_roast")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_roast)
        self.label_type = QtWidgets.QLabel(self.widget)
        self.label_type.setObjectName("label_type")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_type)
        self.lineEdit_type = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_type.setObjectName("lineEdit_type")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_type)
        self.label_taste = QtWidgets.QLabel(self.widget)
        self.label_taste.setObjectName("label_taste")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_taste)
        self.lineEdit_taste = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_taste.setObjectName("lineEdit_taste")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_taste)
        self.label_price = QtWidgets.QLabel(self.widget)
        self.label_price.setObjectName("label_price")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_price)
        self.lineEdit_price = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_price.setObjectName("lineEdit_price")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineEdit_price)
        self.label_volume = QtWidgets.QLabel(self.widget)
        self.label_volume.setObjectName("label_volume")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_volume)
        self.lineEdit_volume = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_volume.setObjectName("lineEdit_volume")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.lineEdit_volume)
        self.verticalLayout.addLayout(self.formLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.okButton = QtWidgets.QPushButton(self.widget)
        self.okButton.setObjectName("okButton")
        self.horizontalLayout.addWidget(self.okButton)
        self.cancelButton = QtWidgets.QPushButton(self.widget)
        self.cancelButton.setObjectName("cancelButton")
        self.horizontalLayout.addWidget(self.cancelButton)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(CoffeeRecord)
        QtCore.QMetaObject.connectSlotsByName(CoffeeRecord)

    def retranslateUi(self, CoffeeRecord):
        _translate = QtCore.QCoreApplication.translate
        CoffeeRecord.setWindowTitle(_translate("CoffeeRecord", "Сорт кофе"))
        self.label_name.setText(_translate("CoffeeRecord", "Название"))
        self.label_roast.setText(_translate("CoffeeRecord", "Обжарка"))
        self.label_type.setText(_translate("CoffeeRecord", "Тип"))
        self.label_taste.setText(_translate("CoffeeRecord", "Вкус"))
        self.label_price.setText(_translate("CoffeeRecord", "Цена"))
        self.label_volume.setText(_translate("CoffeeRecord", "Объём"))
        self.okButton.setText(_translate("CoffeeRecord", "Сохранить"))
        self.cancelButton.setText(_translate("CoffeeRecord", "Отменить"))