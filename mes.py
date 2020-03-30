import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtGui import QIcon, QPixmap
from hola import ploteoCF, ploteoPhF, ploteoZ1Z2, ploteoZF


class Mes(QtWidgets.QMainWindow):
    def __init__(self):
        super(Mes, self).__init__()
        uic.loadUi(r'GUI UI\\pobla.ui', self)
        self.show()

        self.sam = self.findChild(QtWidgets.QComboBox, 'sample')
        self.sam.currentIndexChanged.connect(self.plotTwist)
        self.freq = self.findChild(QtWidgets.QComboBox, 'freq')
        self.freq.currentIndexChanged.connect(self.plotTwist)
        self.dist = self.findChild(QtWidgets.QComboBox, 'distance')
        self.dist.currentIndexChanged.connect(self.plotTwist)
        self.function = self.findChild(QtWidgets.QComboBox, 'function')
        self.function.currentIndexChanged.connect(self.plotTwist)
        self.check = self.findChild(QtWidgets.QCheckBox, 'check')
        self.bt1 = self.findChild(QtWidgets.QPushButton, 'pushButton')
        self.glw = self.findChild(QtWidgets.QOpenGLWidget, 'plotWindow')
        

    def plotTwist(self):
        self.show()
        if self.sam.currentIndex() == 0:
            print("XD")    
            if self.freq.currentIndex() == 0:
                
                if self.dist.currentIndex() == 0:
             
                    if self.function.currentIndex() == 1:
                        print("Vale loco")
        else:
            print("lol")           


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Mes()
    app.exec_()
            
