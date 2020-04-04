import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtGui import QIcon, QPixmap, QPainter
from hola import ploteoCF, ploteoPhF, ploteoZ1Z2, ploteoZF

#Prueba

class Mes(QtWidgets.QMainWindow):
    def __init__(self):
        super(Mes, self).__init__()
        uic.loadUi(r'GUI UI\pobla.ui', self)
        self.show()

        self.sam = self.findChild(QtWidgets.QComboBox, 'cbx')
        self.freq = self.findChild(QtWidgets.QComboBox, 'cbx_2')
        self.dist = self.findChild(QtWidgets.QComboBox, 'cbx_3')
        self.function = self.findChild(QtWidgets.QComboBox, 'cbx_4')
        
        self.check = self.findChild(QtWidgets.QCheckBox, 'check')
        self.bt1 = self.findChild(QtWidgets.QPushButton, 'pushButton')
        self.glw = self.findChild(QtWidgets.QOpenGLWidget, 'myGLWidget')
      #  self.glw.initializeGL()
       # self.glw.defaultFramebufferObject()

        self.sam.currentIndexChanged.connect(self.plotTwist)
        self.freq.currentIndexChanged.connect(self.plotTwist)
        self.dist.currentIndexChanged.connect(self.plotTwist)
        self.function.currentIndexChanged.connect(self.plotTwist)
        self.bt1.clicked.connect(self.buttonClicked)

   # def paintEvent(self, number):
    #    qp = QPainter()
     #   qp.begin(self)
      #  self.glw.ploteoZF(number)
       # qp.end()
    

    def buttonClicked(self):
        self.plotTwist()

    def plotTwist(self):
            #self.glw.makeCurrent()
            if self.sam.currentIndex() == 0:
                if self.freq.currentIndex() == 0:
                    if self.dist.currentIndex() == 0:
                        if self.function.currentIndex() == 0:
                            #ploteoZF(1)
                           #self.glw.paintEvent(self,1)
                        elif self.function.currentIndex() == 1:
                            #ploteoCF(1)
                            self.glw.paintGL(ploteoZF(2))
                        elif self.function.currentIndex() == 2:
                            ploteoZ1Z2(1)
                        elif self.function.currentIndex() == 3:
                            ploteoPhF(1)
                    elif self.dist.currentIndex() == 1:
                        if self.function.currentIndex() == 0:
                            print("0 0 1 0")
                        elif self.function.currentIndex() == 1:
                            print("0 0 1 1")
                        elif self.function.currentIndex() == 2:
                            print("0 0 1 2")
                        elif self.function.currentIndex() == 3:
                            print("0 0 1 3")    
                    elif self.dist.currentIndex() == 2: 
                        if self.function.currentIndex() == 0:
                            print("0 0 2 0")
                        elif self.function.currentIndex() == 1:
                            print("0 0 2 1")
                        elif self.function.currentIndex() == 2:
                            print("0 0 2 2")
                        elif self.function.currentIndex() == 3:
                            print("0 0 2 3")    
                elif self.freq.currentIndex() == 1:
                    if self.dist.currentIndex() == 0:
                        if self.function.currentIndex() == 0:
                            print("0 1 0 0")
                        elif self.function.currentIndex() == 1:
                            print("0 1 0 1")
                        elif self.function.currentIndex() == 2:
                            print("0 1 0 2")
                        elif self.function.currentIndex() == 3:
                            print("0 1 0 3")
                    elif self.dist.currentIndex() == 1:
                        if self.function.currentIndex() == 0:
                            print("0 1 1 0")
                        elif self.function.currentIndex() == 1:
                            print("0 1 1 1")
                        elif self.function.currentIndex() == 2:
                            print("0 1 1 2")
                        elif self.function.currentIndex() == 3:
                            print("0 1 1 3")    
                    elif self.dist.currentIndex() == 2: 
                        if self.function.currentIndex() == 0:
                            print("0 1 2 0")
                        elif self.function.currentIndex() == 1:
                            print("0 1 2 1")
                        elif self.function.currentIndex() == 2:
                            print("0 1 2 2")  
                        elif self.function.currentIndex() == 3:
                            print("0 1 2 3")
                elif self.freq.currentIndex() == 2:
                    if self.dist.currentIndex() == 0:
                        if self.function.currentIndex() == 0:
                            print("0 2 0 0")
                        elif self.function.currentIndex() == 1:
                            print("0 2 0 1")
                        elif self.function.currentIndex() == 2:
                            print("0 2 0 2")
                        elif self.function.currentIndex() == 3:
                            print("0 2 0 3")
                    elif self.dist.currentIndex() == 1:
                        if self.function.currentIndex() == 0:
                            print("0 2 1 0")
                        elif self.function.currentIndex() == 1:
                            print("0 2 1 1")
                        elif self.function.currentIndex() == 2:
                            print("0 2 1 2")
                        elif self.function.currentIndex() == 3:
                            print("0 2 1 3")    
                    elif self.dist.currentIndex() == 2: 
                        if self.function.currentIndex() == 0:
                            print("0 2 2 0")
                        elif self.function.currentIndex() == 1:
                            print("0 2 2 1")
                        elif self.function.currentIndex() == 2:
                            print("0 2 2 2")  
                        elif self.function.currentIndex() == 3:
                            print("0 2 2 3")            
            elif self.sam.currentIndex() == 1:
                if self.freq.currentIndex() == 0:
                    if self.dist.currentIndex() == 0:
                        if self.function.currentIndex() == 0:
                            print("1 0 0 0")
                        elif self.function.currentIndex() == 1:
                            print("1 0 0 1")
                        elif self.function.currentIndex() == 2:
                            print("1 0 0 2")
                        elif self.function.currentIndex() == 3:
                            print("1 0 0 3")
                    elif self.dist.currentIndex() == 1:
                        if self.function.currentIndex() == 0:
                            print("1 0 1 0")
                        elif self.function.currentIndex() == 1:
                            print("1 0 1 1")
                        elif self.function.currentIndex() == 2:
                            print("1 0 1 2")
                        elif self.function.currentIndex() == 3:
                            print("1 0 1 3")    
                    elif self.dist.currentIndex() == 2: 
                        if self.function.currentIndex() == 0:
                            print("1 0 2 0")
                        elif self.function.currentIndex() == 1:
                            print("1 0 2 1")
                        elif self.function.currentIndex() == 2:
                            print("1 0 2 2")
                        elif self.function.currentIndex() == 3:
                            print("1 0 2 3")    
                elif self.freq.currentIndex() == 1:
                    if self.dist.currentIndex() == 0:
                        if self.function.currentIndex() == 0:
                            print("1 1 0 0")
                        elif self.function.currentIndex() == 1:
                            print("1 1 0 1")
                        elif self.function.currentIndex() == 2:
                            print("1 1 0 2")
                        elif self.function.currentIndex() == 3:
                            print("1 1 0 3")
                    elif self.dist.currentIndex() == 1:
                        if self.function.currentIndex() == 0:
                            print("1 1 1 0")
                        elif self.function.currentIndex() == 1:
                            print("1 1 1 1")
                        elif self.function.currentIndex() == 2:
                            print("1 1 1 2")
                        elif self.function.currentIndex() == 3:
                            print("1 1 1 3")    
                    elif self.dist.currentIndex() == 2: 
                        if self.function.currentIndex() == 0:
                            print("1 1 2 0")
                        elif self.function.currentIndex() == 1:
                            print("1 1 2 1")
                        elif self.function.currentIndex() == 2:
                            print("1 1 2 2")  
                        elif self.function.currentIndex() == 3:
                            print("1 1 2 3")
                elif self.freq.currentIndex() == 2:
                    if self.dist.currentIndex() == 0:
                        if self.function.currentIndex() == 0:
                            print("1 2 0 0")
                        elif self.function.currentIndex() == 1:
                            print("1 2 0 1")
                        elif self.function.currentIndex() == 2:
                            print("1 2 0 2")
                        elif self.function.currentIndex() == 3:
                            print("1 2 0 3")
                    elif self.dist.currentIndex() == 1:
                        if self.function.currentIndex() == 0:
                            print("1 2 1 0")
                        elif self.function.currentIndex() == 1:
                            print("1 2 1 1")
                        elif self.function.currentIndex() == 2:
                            print("1 2 1 2")
                        elif self.function.currentIndex() == 3:
                            print("1 2 1 3")    
                    elif self.dist.currentIndex() == 2: 
                        if self.function.currentIndex() == 0:
                            print("1 2 2 0")
                        elif self.function.currentIndex() == 1:
                            print("1 2 2 1")
                        elif self.function.currentIndex() == 2:
                            print("1 2 2 2")  
                        elif self.function.currentIndex() == 3:
                            print("1 2 2 3")
            elif self.sam.currentIndex() == 2:
                if self.freq.currentIndex() == 0:
                    if self.dist.currentIndex() == 0:
                        if self.function.currentIndex() == 0:
                            print("2 0 0 0")
                        elif self.function.currentIndex() == 1:
                            print("2 0 0 1")
                        elif self.function.currentIndex() == 2:
                            print("2 0 0 2")
                        elif self.function.currentIndex() == 3:
                            print("2 0 0 3")
                    elif self.dist.currentIndex() == 1:
                        if self.function.currentIndex() == 0:
                            print("2 0 1 0")
                        elif self.function.currentIndex() == 1:
                            print("2 0 1 1")
                        elif self.function.currentIndex() == 2:
                            print("2 0 1 2")
                        elif self.function.currentIndex() == 3:
                            print("2 0 1 3")    
                    elif self.dist.currentIndex() == 2: 
                        if self.function.currentIndex() == 0:
                            print("2 0 2 0")
                        elif self.function.currentIndex() == 1:
                            print("2 0 2 1")
                        elif self.function.currentIndex() == 2:
                            print("2 0 2 2")
                        elif self.function.currentIndex() == 3:
                            print("2 0 2 3")    
                elif self.freq.currentIndex() == 1:
                    if self.dist.currentIndex() == 0:
                        if self.function.currentIndex() == 0:
                            print("2 1 0 0")
                        elif self.function.currentIndex() == 1:
                            print("2 1 0 1")
                        elif self.function.currentIndex() == 2:
                            print("2 1 0 2")
                        elif self.function.currentIndex() == 3:
                            print("2 1 0 3")
                    elif self.dist.currentIndex() == 1:
                        if self.function.currentIndex() == 0:
                            print("2 1 1 0")
                        elif self.function.currentIndex() == 1:
                            print("2 1 1 1")
                        elif self.function.currentIndex() == 2:
                            print("2 1 1 2")
                        elif self.function.currentIndex() == 3:
                            print("2 1 1 3")    
                    elif self.dist.currentIndex() == 2: 
                        if self.function.currentIndex() == 0:
                            print("2 1 2 0")
                        elif self.function.currentIndex() == 1:
                            print("2 1 2 1")
                        elif self.function.currentIndex() == 2:
                            print("2 1 2 2")  
                        elif self.function.currentIndex() == 3:
                            print("2 1 2 3")
                elif self.freq.currentIndex() == 2:
                    if self.dist.currentIndex() == 0:
                        if self.function.currentIndex() == 0:
                            print("2 2 0 0")
                        elif self.function.currentIndex() == 1:
                            print("2 2 0 1")
                        elif self.function.currentIndex() == 2:
                            print("2 2 0 2")
                        elif self.function.currentIndex() == 3:
                            print("2 2 0 3")
                    elif self.dist.currentIndex() == 1:
                        if self.function.currentIndex() == 0:
                            print("2 2 1 0")
                        elif self.function.currentIndex() == 1:
                            print("2 2 1 1")
                        elif self.function.currentIndex() == 2:
                            print("2 2 1 2")
                        elif self.function.currentIndex() == 3:
                            print("2 2 1 3")    
                    elif self.dist.currentIndex() == 2: 
                        if self.function.currentIndex() == 0:
                            print("2 2 2 0")
                        elif self.function.currentIndex() == 1:
                            print("2 2 2 1")
                        elif self.function.currentIndex() == 2:
                            print("2 2 2 2")  
                        elif self.function.currentIndex() == 3:
                            print("2 2 2 3")                
            else:
                print("CORONAO")

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Mes()
    app.exec_()
            
