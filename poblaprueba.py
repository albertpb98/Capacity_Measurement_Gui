import sys
from PyQt5 import QtWidgets, uic
from hola import ploteoZF, ploteoPhF, ploteoCF, ploteoZ1Z2

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi(r'C:\Users\apb19\Documents\PAE\GUI UI\Test.ui', self)
        self.show()
        items = ["10Hz", "1Hz", "0.1Hz"]
        self.cbx=self.findChild(QtWidgets.QComboBox, 'comboBox')
        self.cbx.addItems(items)
        self.list = self.findChild(QtWidgets.QListWidget, 'listWidget')
        self.list.addItems(["Z(F)", "Ph(f)", "Z1(Z2)", "C(f)"])
        self.cbx.currentIndexChanged.connect(self.liststate)
        self.list.itemDoubleClicked.connect(self.itemSelected)
        #self.button = self.findChild(QtWidgets.QPushButton, 'pushButton') Codigo para el boton que no usamos
        #self.button.setCheckable(True)
        #self.button.pressed.connect(self.liststate)

    def liststate(self):
        #if self.button.isChecked():
            self.list.clear()
            if self.cbx.currentIndex() == 0:
                litems = ["Z(F)", "Ph(f)", "Z1(Z2)", "C(f)"]
                #print("MM")
            elif self.cbx.currentIndex() == 1:
                #print("M1")
                litems = ["Z(F)", "Ph(f)", "Z1(Z2)", "C(f)"]
            elif self.cbx.currentIndex() == 2:
                litems = ["Z(F)", "Ph(f)", "Z1(Z2)", "C(f)"]
                #print("M2")
            else:
                print("Cyka Blyat")
            self.list.addItems(litems)

    def itemSelected(self):
        number = self.cbx.currentIndex() 
        if number == 0:
            if self.list.currentRow() == 0:
                ploteoZF(1)
            elif self.list.currentRow() == 1:
                ploteoPhF(1)
            elif self.list.currentRow() == 2:
                ploteoZ1Z2(1)
            elif self.list.currentRow() == 3:
                ploteoCF(1)

        elif number == 1:
            if self.list.currentRow() == 0:
                ploteoZF(2)
                
            elif self.list.currentRow() == 1:
                ploteoPhF(2)
                
            elif self.list.currentRow() == 2:
                ploteoZ1Z2(2)
                
            elif self.list.currentRow() == 3:
                ploteoCF(2)
                
        elif number == 2:
            if self.list.currentRow() == 0:
                ploteoZF(3)
            elif self.list.currentRow() == 1:
                ploteoPhF(3)
            elif self.list.currentRow() == 2:
                ploteoZ1Z2(3)
            elif self.list.currentRow() == 3:
                ploteoCF(3)
   
            
   
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    app.exec_()
            