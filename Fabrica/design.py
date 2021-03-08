# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fabr.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(526, 352)
        MainWindow.setWindowTitle('Управление Фабрикой')
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 71, 41))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 71, 41))
        self.label_2.setObjectName("label_2")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(90, 60, 401, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setRange(0, 300)
        self.progressBar.setObjectName("progressBar")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(70, 100, 111, 41))
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(40, 140, 71, 31))
        self.label_5.setObjectName("label_5")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(340, 100, 71, 41))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(40, 180, 81, 31))
        self.label_8.setObjectName("label_8")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(310, 140, 71, 31))
        self.label_6.setObjectName("label_6")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(310, 170, 81, 31))
        self.label_9.setObjectName("label_9")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(60, 210, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(310, 210, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(320, 250, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setObjectName("pushButton_3")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate(
            "MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Деньги: </span></p></body></html>"))
        self.label_2.setText(_translate(
            "MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Склад</span></p></body></html>"))
        self.label_3.setText(_translate(
            "MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; text-decoration: underline;\">Метериалы</span></p></body></html>"))
        self.label_5.setText(_translate(
            "MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Стоимость</span></p></body></html>"))
        self.label_7.setText(_translate(
            "MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; text-decoration: underline;\">Товары</span></p></body></html>"))
        self.label_8.setText(_translate(
            "MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Количество</span></p></body></html>"))
        self.label_6.setText(_translate(
            "MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Стоимость</span></p></body></html>"))
        self.label_9.setText(_translate(
            "MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Количество</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Купить"))
        self.pushButton_2.setText(_translate("MainWindow", "Произвести"))
        self.pushButton_3.setText(_translate("MainWindow", "Продать"))
