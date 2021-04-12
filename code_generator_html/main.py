import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QColorDialog, QFontDialog
import dis


class ExampleApp(QtWidgets.QMainWindow, dis.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('html5.png'))
        self.pushButton_2.clicked.connect(self.bold)
        self.pushButton.clicked.connect(self.save_file_html)
        self.pushButton_6.clicked.connect(self.get_color)
        self.pushButton_7.clicked.connect(self.get_font)
        self.pushButton_8.clicked.connect(self.font_dialog)

        # Меню
        self.action_3.triggered.connect(lambda: self.close())
        self.action_5.triggered.connect(self.save_file_html)
        self.action.triggered.connect(self.save_file_txt)
        self.action_2.triggered.connect(self.load_file_txt)

    def save_file_html(self):
        filename = QFileDialog.getSaveFileName(
            self, 'Сохранить в html файл', '', "Html Files (*.html);;All Files (*)")[0]
        if filename == '':
            print('Error')
        else:
            file = open(filename, 'w')
            text = self.textEdit.toPlainText()
            title = '''<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
</head>
<body>
'''
            foter = '''\n</body>
</html>
'''
            file.write(title + text + foter)
            file.close()

    def save_file_txt(self):
        filename = QFileDialog.getSaveFileName(
            self, 'Сохранение файла', '', "Txt Files (*.txt);;All Files (*)")[0]
        if filename == '':
            print('Error')
        else:
            file = open(filename, 'w')
            text = self.textEdit.toPlainText()
            file.write(text)
            file.close()

    def load_file_txt(self):
        filename = QFileDialog.getOpenFileName(
            self, 'Загрузка файла', '', "Txt Files (*.txt);;All Files (*)")[0]
        if filename == '':
            print('Error')
        else:
            file = open(filename, 'r')
            text = file.readlines()
            file.close()
            self.textEdit.setPlainText(str(text))

    def bold(self):
        if self.pushButton_2.isChecked():
            self.textEdit.insertPlainText('<b>')
        else:
            self.textEdit.insertPlainText('</b>')

    def get_color(self):
        color = QColorDialog.getColor(
            QtGui.QColor('#000000'), self, 'Выбор цвета')
        if color.isValid():
            print(color.name())

    def get_font(self):
        font = self.fontComboBox.currentText()
        size_font = self.spinBox.value()
        print('Шрифт', font, type(font))
        print('Размерт', size_font, type(size_font))

    def font_dialog(self):
        # Возращает кортеж [0] - шрифт [1] - статус
        font_d, status = QFontDialog.getFont(
            QtGui.QFont('Arial', 8), self, 'Выбор шрифта')
        if status:
            print(font_d.family(), font_d.pointSize(),
                  font_d.weight(), font_d.italic(), font_d.underline())


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
