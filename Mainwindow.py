import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtGui import QIcon, QPixmap

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi(r'GUI UI\mainwindow.ui', self)
        
        self.b1 = self.findChild(QtWidgets.QPushButton, 'pushButton')
        self.b1.setCheckable(True)
        self.b5 = self.findChild(QtWidgets.QPushButton, 'BtMenu')
        self.b2 = self.findChild(QtWidgets.QPushButton, 'pushButton_2')
        self.b3 = self.findChild(QtWidgets.QPushButton, 'pushButton_3')
        self.b4 = self.findChild(QtWidgets.QPushButton, 'pushButton_4')
        self.creditext = self.findChild(QtWidgets.QLabel, 'CreditosTexto')
        self.ccl = self.findChild(QtWidgets.QLabel, 'CCLicense')
        self.etocha = self.findChild(QtWidgets.QLabel, 'EGorda')
        self.l1 = self.findChild(QtWidgets.QLabel, 'titulo')
        self.l2 = self.findChild(QtWidgets.QLabel, 'background')
        

        pixmap = QPixmap(r'GUI Images\main gui.png')
        ccimage =QPixmap(r'GUI Images\CC.png')
        egorda = QPixmap(r'GUI Images\seal.png')
        self.l2.setPixmap(pixmap)
        self.ccl.setPixmap(ccimage)
        self.etocha.setPixmap(egorda)

        self.ccl.hide()
        self.b5.hide()
        self.etocha.hide()
        self.creditext.hide()

        self.b1.clicked.connect(self.b1clicked)
        self.b2.clicked.connect(self.b2clicked)
        self.b3.clicked.connect(self.b3clicked)
        self.b4.clicked.connect(self.b4clicked)
        self.b5.clicked.connect(self.bmclicked)
        self.show()

    def b1clicked(self):
        print("Clicaste el b1")
    def b2clicked(self):
        print("Clicaste el b2")
    def b3clicked(self):
        print("Clicaste el b3")
    def b4clicked(self):
        self.b1.hide()
        self.b2.hide()
        self.b3.hide()
        self.b4.hide()
        self.l1.hide()
        self.ccl.show()
        self.b5.show()
        self.etocha.show()
        self.creditext.show()
        #print("Clicaste el b4")
    def bmclicked(self):
        self.b1.show()
        self.b2.show()
        self.b3.show()
        self.b4.show()
        self.l1.show()
        self.ccl.hide()
        self.b5.hide()
        self.etocha.hide()
        self.creditext.hide()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    app.exec_()
            