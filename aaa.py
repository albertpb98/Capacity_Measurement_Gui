import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QPushButton, QComboBox, QStyleFactory, QListWidget, \
    QTableWidget, QTableWidgetItem, QListWidgetItem


class Example(QWidget):
    def __init__(self, parent=None):
        super(Example, self).__init__(parent)
        QApplication.setStyle(QStyleFactory.create('Fusion'))

        # -------------- QCOMBOBOX ----------------------
        cbx = QComboBox()
        # agregar lista de nombres de estilos disponibles
        cbx.addItems(QStyleFactory.keys())
        # responder al evento cambio de texto
        cbx.currentTextChanged.connect(self.textChanged)
        # seleccionar el ultimo elemento
        cbx.setItemText(4, 'Fusion')

        # -------------- QLISTWIDGET ---------------------
        items = ['Ubuntu', 'Linux', 'Mac OS', 'Windows', 'Fedora', 'Chrome OS', 'Android', 'Windows Phone']

        self.lv = QListWidget()
        self.lv.addItems(items)
        self.lv.itemSelectionChanged.connect(self.itemChanged)

        

        vbx = QVBoxLayout()
        vbx.addWidget(QPushButton('Tutoriales PyQT-5'))
        vbx.setAlignment(Qt.AlignTop)
        vbx.addWidget(cbx)
        vbx.addWidget(self.lv)


        self.setWindowTitle("Items View")
        self.resize(362, 320)
        self.setLayout(vbx)

    def textChanged(self, txt):
        QApplication.setStyle(QStyleFactory.create(txt))

    def itemChanged(self):
        item = QListWidgetItem(self.lv.currentItem())
        print("Sistema seleccionado: ", item.text())



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ejm = Example()
    ejm.show()
    sys.exit(app.exec_())