import sys  # sys нужен для передачи argv в QApplication
from random import randint
from PyQt5 import QtWidgets
import design  # Это наш преобразованный файл дизайна


class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Это для инициализации дизайна
        global money, price_material, price_product, sklad, material, product
        money = 1000
        sklad, material, product = 0, 0, 0
        price_material, price_product = randint(50, 100), randint(70, 120)
        self.label.setText('Деньги: ' + str(money))
        self.label_8.setText('Количество: ' + str(material))
        self.label_5.setText('Стоимость: ' + str(price_material))
        self.label_9.setText('Количество: ' + str(product))
        self.label_6.setText('Стоимость: ' + str(price_product))
        self.pushButton.clicked.connect(self.by_material)

    def by_material(self):
        global money, price_material, price_product, sklad, material, product
        if (money >= price_material) and (sklad <= 297):
            material += 3
            sklad += 3
            money -= price_material
            self.label.setText('Деньги: ' + str(money))
            self.label_8.setText('Количество: ' + str(material))
            self.label_5.setText('Стоимость: ' + str(price_material))
            self.progressBar.setValue(sklad)


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение


if __name__ == '__main__':
    main()
