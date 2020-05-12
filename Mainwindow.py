import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtGui import QIcon, QPixmap
from Plotter import ploteoCF, ploteoPhF, ploteoZ1Z2, ploteoZF
from TouchSensor import ComportAvailable

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi(r'GUI UI\mainwindow.ui', self)
        self.setWindowTitle('Capacity Measurement User Interface')
        self.b1 = self.findChild(QtWidgets.QPushButton, 'pushButton')
        #self.b1.setCheckable(True)
        self.bconnect = self.findChild(QtWidgets.QPushButton, 'pushButton_5')
        self.COMLabel = self.findChild(QtWidgets.QLabel, 'COMPorts')
        self.COMBox = self.findChild(QtWidgets.QComboBox, 'COMPortsL')
        self.list = self.findChild(QtWidgets.QListView, 'ListTouch')
        self.b5 = self.findChild(QtWidgets.QPushButton, 'BtMenu')
        self.b2 = self.findChild(QtWidgets.QPushButton, 'pushButton_2')
        self.b3 = self.findChild(QtWidgets.QPushButton, 'pushButton_3')
        self.b4 = self.findChild(QtWidgets.QPushButton, 'pushButton_4')
        self.creditext = self.findChild(QtWidgets.QLabel, 'CreditosTexto')
        self.ccl = self.findChild(QtWidgets.QLabel, 'CCLicense')
        self.etocha = self.findChild(QtWidgets.QLabel, 'EGorda')
        self.github = self.findChild(QtWidgets.QLabel, 'github')
        self.l1 = self.findChild(QtWidgets.QLabel, 'titulo')
        self.l2 = self.findChild(QtWidgets.QLabel, 'background')
        self.tdist = self.findChild(QtWidgets.QLabel, 'tdist')
        self.tfreq = self.findChild(QtWidgets.QLabel, 'tfreq')
        self.tsample = self.findChild(QtWidgets.QLabel, 'tsample')
        self.tplot = self.findChild(QtWidgets.QLabel, 'tplot')
        self.b1text = self.findChild(QtWidgets.QLabel, 'b1text')
        self.sample = self.findChild(QtWidgets.QComboBox, 'Muestras')
        self.freq = self.findChild(QtWidgets.QComboBox, 'Freq')
        self.dist = self.findChild(QtWidgets.QComboBox, 'dist')
        self.plot = self.findChild(QtWidgets.QComboBox, 'plot')
        self.bplot = self.findChild(QtWidgets.QPushButton, 'bplot')

        pixmap = QPixmap(r'GUI Images\main gui.png')
        ccimage =QPixmap(r'GUI Images\CC.png')
        egorda = QPixmap(r'GUI Images\seal.png')
        git = QPixmap(r'GUI Images\githublogo.png')
        self.github.setPixmap(git)
        self.l2.setPixmap(pixmap)
        self.ccl.setPixmap(ccimage)
        self.etocha.setPixmap(egorda)

        #B4
        self.ccl.hide()
        self.b5.hide()
        self.etocha.hide()
        self.creditext.hide()
        self.github.hide()
        #B1
        self.tfreq.hide()
        self.tsample.hide()
        self.tplot.hide()
        self.tdist.hide()
        self.sample.hide()
        self.freq.hide()
        self.dist.hide()
        self.plot.hide()
        self.b1text.hide()
        self.bplot.hide()

        #B2
        self.COMBox.hide()
        self.COMLabel.hide()
        self.bconnect.hide()
        self.list.hide()

        self.b1.clicked.connect(self.b1clicked)
        self.b2.clicked.connect(self.b2clicked)
        self.b3.clicked.connect(self.b3clicked)
        self.b4.clicked.connect(self.b4clicked)
        self.b5.clicked.connect(self.bmclicked)
        self.bplot.clicked.connect(self.bplotclicked)
        self.show()

    def b1clicked(self):
        self.b1.hide()
        self.b2.hide()
        self.b3.hide()
        self.b4.hide()
        self.l1.hide()
        self.b5.show()
        self.tfreq.show()
        self.tsample.show()
        self.tplot.show()
        self.tdist.show()
        self.sample.show()
        self.freq.show()
        self.dist.show()
        self.plot.show()
        self.b1text.show()
        self.bplot.show()

    def b2clicked(self):
        self.b1.hide()
        self.b2.hide()
        self.b3.hide()
        self.b4.hide()
        self.l1.hide()
        self.b5.show()
        self.COMBox.show()
        self.COMLabel.show()
        self.bconnect.show()
        self.list.show()
        self.COMBox.addItems(ComportAvailable())


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
        self.github.show()
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
        self.tfreq.hide()
        self.tsample.hide()
        self.tplot.hide()
        self.tdist.hide()
        self.sample.hide()
        self.freq.hide()
        self.dist.hide()
        self.plot.hide()
        self.b1text.hide()
        self.bplot.hide()
        self.github.hide()
        self.COMBox.hide()
        self.COMLabel.hide()
        self.bconnect.hide()
        self.list.hide()


    def bplotclicked(self):
        numsamples = self.sample.currentIndex()
        numfreq = self.freq.currentIndex()
        numdist = self.dist.currentIndex()
        numplot =self.plot.currentIndex()

        if numplot == 0: #Ploteas Z(F)
            ploteoZF(numsamples, numfreq, numdist)
        elif numplot == 1: #Ploteas Ph(f)
            ploteoPhF(numsamples, numfreq, numdist)
        elif numplot == 2:
            ploteoZ1Z2(numsamples, numfreq, numdist)
        elif numplot == 3:
            ploteoCF(numsamples, numfreq, numdist)



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QIcon(r'GUI Images\icoUpc.png'))
    window = Ui()
    app.exec_()
            
