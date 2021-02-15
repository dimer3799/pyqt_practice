import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets, QtGui
import button  # Это наш преобразованный файл дизайна
class ExampleApp(QtWidgets.QMainWindow, button.Ui_MainWindow):
    def __init__(self):
    # Это здесь нужно для доступа к переменным, методам
    # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)# Это для инициализации дизайна

        text = self.label.text()
        #self.label_2.setText('<center><span style=\" font-size:25pt; color:#01ff1e;\">'+text+'</span></center>')
        #self.label.setPixmap((QtGui.Qpixmap('1.png')))

        #self.pushButton.clicked.connect(self.edit)
        #self.pushButton.pressed.connect(self.edit)
        #
        self.pushButton.released.connect(self.edit)

    def edit(self):
        # Обработчик
        self.label_2.setText('На кнопку нажали')

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
