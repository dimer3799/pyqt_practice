import sys  # sys нужен для передачи argv в QApplication
from random import randint
from PyQt5 import QtWidgets, QtGui
import menu  # Это наш преобразованный файл дизайна


class ExampleApp(QtWidgets.QMainWindow, menu.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Это для инициализации дизайна
        self.action.triggered.connect(self.cliked)

        self.action_exit.triggered.connect(lambda: self.close())

        # Вызов метода с lambda - мы можем передовать параметр
        # lambda вызывает функцию и можем передать параметр
        self.action_2.triggered.connect(
            lambda: self.cliked_l('Сохранения файла'))
        self.action_3.triggered.connect(
            lambda: self.cliked_l('Копирование данных'))
        self.action_4.triggered.connect(
            lambda: self.cliked_l('Вставка данных'))

    def cliked(self, text):
        self.label.setText('Новый файл')
        self.label.adjustSize()

    def cliked_l(self, text):
        self.label.setText(text)
        self.label.adjustSize()


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение


if __name__ == '__main__':
    main()
