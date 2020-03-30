import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtGui import QIcon, QPixmap

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi(r'GUI UI\mainwindow.ui', self)
        pixmap = QPixmap(r"GUI Images\main gui.png")
        self.b1 = self.findChild(QtWidgets.QPushButton, 'pushButton')
        self.l2 = self.findChild(QtWidgets.QLabel, 'label')
        self.l2.setPixmap(pixmap)
        self.show()
        
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    app.exec_()
            