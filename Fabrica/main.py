import sys  # sys нужен для передачи argv в QApplication
from random import randint
from PyQt5 import QtWidgets, QtGui
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
        self.pushButton_2.clicked.connect(self.farm_product)
        self.pushButton_3.clicked.connect(self.sell_product)

    def by_material(self):
        global money, price_material, sklad, material
        if (money >= price_material) and (sklad <= 297):
            material += 1
            sklad += 1
            money -= price_material
            self.label.setText('Деньги: ' + str(money))
            self.label_8.setText('Количество: ' + str(material))
            self.label_5.setText('Стоимость: ' + str(price_material))
            self.progressBar.setValue(sklad)

    def farm_product(self):
        global money, sklad, material, product
        if material >= 5:
            material -= 5
            sklad -= 2
            product += 3
            self.label_8.setText('Количество: ' + str(material))
            self.label_9.setText('Количество: ' + str(product))
            self.progressBar.setValue(sklad)

    def sell_product(self):
        global money,  price_product, sklad, product
        if product >= 1:
            money += price_product
            sklad -= 1
            product -= 1
            self.label_8.setText('Количество: ' + str(material))
            self.label_9.setText('Количество: ' + str(product))
            self.label.setText('Деньги: ' + str(money))
            self.progressBar.setValue(sklad)
        else:
            QtWidgets.QMessageBox.information(
                None, 'Сообщене', 'Не хватает продукции')


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение


if __name__ == '__main__':
    main()
