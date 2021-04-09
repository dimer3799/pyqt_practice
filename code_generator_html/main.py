import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
import dis


class ExampleApp(QtWidgets.QMainWindow, dis.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.bold)
        self.pushButton.clicked.connect(self.save_file)

    def save_file(self):
        filename = QFileDialog.getSaveFileName(
            self, 'Save Lattice', '', "Html Files (*.html);;All Files (*)")[0]
        if filename == '':
            print('Error')
        else:
            file = open(filename, 'w')
            text = self.textEdit.toPlainText()
            file.write(text)
            file.close()

    def bold(self):
        if self.pushButton_2.isChecked():
            self.textEdit.insertPlainText('<b>')
        else:
            self.textEdit.insertPlainText('</b>')


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
