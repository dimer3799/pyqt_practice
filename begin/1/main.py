import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets
import test  # Это наш преобразованный файл дизайна
class ExampleApp(QtWidgets.QMainWindow, test.Ui_MainWindow):
    def __init__(self):
    # Это здесь нужно для доступа к переменным, методам
    # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)# Это для инициализации дизайна

def main():
    app = QtWidgets.QApplication(sys.argv)
    # Новый экземплярQApplication
    window = ExampleApp()
    # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

if __name__ == '__main__':
# Если мы запускаем файл напрямую,а не импортируем
    main()  # то запускаем функцию main()
