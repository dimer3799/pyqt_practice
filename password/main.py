import sys, password_form
from PyQt5 import QtWidgets, QtGui

class ExampleApp(QtWidgets.QMainWindow, password_form.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.setFlat(True)
        self.pushButton.clicked.connect(self.clic)
    def clic(self):
        login = self.lineEdit.text()
        pswd = self.lineEdit_2.text()

        if (login == 'dimer') and pswd == 'dimerr':
            self.lineEdit.clear()
            self.lineEdit_2.clear()
            self.label_3.setText('Пароль верный')
        else:
            self.label_3.setText('Неверный пароль')
            self.lineEdit.clear()
            self.lineEdit_2.clear()

	#def increase(self):
	#	self.label.setText(str(int(self.label.text())+1))

	#def decrease(self):
	#	self.label.setText(str(int(self.label.text())-1))

def main():
	windows = QtWidgets.QApplication(sys.argv)

	my_win = ExampleApp()
	my_win.show()
	windows.exec_()

if __name__ == '__main__':
	main()
