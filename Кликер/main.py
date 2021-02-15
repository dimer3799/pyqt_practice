from PyQt5 import QtWidgets
import sys, form

class Cliker(QtWidgets.QMainWindow, form.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.clic)
        self.pushButton_2.clicked.connect(self.sbros)
        global a
        a = 0

    def clic(self):
        global a
        a +=1
        self.label_2.setText(str(a))

    def sbros(self):
        global a
        a = 0
        self.label_2.setText(str(a))

def main():
    windows = QtWidgets.QApplication(sys.argv)
    my_win = Cliker()
    my_win.show()
    windows.exec_()

if __name__ == '__main__':
	main()
