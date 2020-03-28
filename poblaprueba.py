import sys
from PyQt5 import QtWidgets, uic

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('Test.ui', self)
        self.show()
        items = ["MM", "M1", "M2"]
        self.cbx=self.findChild(QtWidgets.QComboBox, 'comboBox')
        self.cbx.addItems(items)
        self.list = self.findChild(QtWidgets.QListWidget, 'listWidget')
        self.list.addItems(["MM", "M1", "M2"])
        self.cbx.currentIndexChanged.connect(self.liststate)
        #self.button = self.findChild(QtWidgets.QPushButton, 'pushButton') Codigo para el boton que no usamos
        #self.button.setCheckable(True)
        #self.button.pressed.connect(self.liststate)

    def liststate(self):
        #if self.button.isChecked():
            self.list.clear()
            if self.cbx.currentIndex() == 0:
                litems = ["XD", "MM", "XD"]
                #print("MM")
            elif self.cbx.currentIndex() == 1:
                #print("M1")
                litems = ["Xd", "M1", "Xd"]
            elif self.cbx.currentIndex() == 2:
                litems = ["xD", "M2", "xD"]
                #print("M2")
            else:
                print("Cyka Blyat")
            self.list.addItems(litems)
      
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    app.exec_()
            