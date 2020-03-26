
import sys
import os

from PyQt5.QtGui import QPainter, QFont, QColor, QPixmap, QPen, QBrush, QIcon
from PyQt5.QtCore import Qt, QRect, QPoint
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QLabel, QLineEdit, QMainWindow, qApp, QAction
from hola import ploteo
from dataframe import Nanotech as nano

#class Example(QMainWindow):
class Example(nano):
    def __init__(self):
        #super().__init__()
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        self.resize(1280, 720)
        self.setWindowTitle('PAE Biorobotics')

        exitAction = QAction(QIcon("exit.png"), "&Exit", self)
        exitAction.setShortcut("Ctrl+Q")
        exitAction.triggered.connect(qApp.quit)

        #menubar = self.menuBar()

        #fileMenu = menubar.addMenu("&File")
        #fileMenu.addAction(exitAction)

        #copyAction = QAction(QIcon('copy.png'), 'Copy', self)
        #pasteAction = QAction(QIcon('paste.png'), 'Paste', self)
        #cutAction = QAction(QIcon('cut.png'), 'Cut', self)

        #editMenu = menubar.addMenu("Edit")
        #editMenu.addAction(copyAction)
        #editMenu.addAction(pasteAction)
        #editMenu.addAction(cutAction)

        #findMenu = editMenu.addMenu(QIcon('image/find_disabled.png'), 'Find')

        #findAction = QAction('Find', self)
        #findAction.setShortcut('Ctrl+F')
        #findAction.setStatusTip('Buscar texto indicado')

        #replaceAction = QAction('Replace', self)
        #replaceAction.setShortcut('Ctrl+R')
        #replaceAction.setStatusTip('Reemplazar texto seleccionado')

        #findMenu.addAction(findAction)
        #findMenu.addAction(replaceAction)

        #aboutAction = QAction('&About', self)
        #helpMenu = menubar.addMenu('&Help')
        #helpMenu.addAction(aboutAction)


        btn1 = QPushButton("Nanotech", self)
        btn1.resize(250,40)
        btn1.move(400/2-150/2,200/2-40)
        btn1.clicked.connect(self.buttonClicked)    
    
        btn2 = QPushButton("Impedance Measurements",self)
        btn2.resize(250,40)
        btn2.move(400/2-150/2,200/2)
        btn2.clicked.connect(self.buttonClicked)

        btn3 = QPushButton("Optic Fiber",self)
        btn3.resize(250,40)
        btn3.move(400/2-150/2,200/2+40)
        btn3.clicked.connect(self.buttonClicked)

        self.show()


    def buttonClicked(self,e):
        btn_txt = self.sender().text()
        if btn_txt == "Nanotech":
            os.system('NOTEPAD.exe')
        elif btn_txt == "Impedance Measurements":
            self.NewWindow1 = nano()
        elif btn_txt == "Optic Fiber":
            QMessageBox.information(self,"Welcome","You have clicked on: " + btn_txt)


    def closeEvent(self,event):
        reply = QMessageBox.question(self,
                                        "Close app", "Do you really want to close the app?",
                                        QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Escape:
            self.close()                        


    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        #self.drawImage(event, qp, r'C:\Users\apb19\Desktop\etsetb.jpg')
        self.drawImage(event, qp, r'C:\\Users\\alexa\\OneDrive\\Escritorio\\squad')
        self.drawText(event, qp, 'EL PAE CHAVALES')
        qp.end()

    
    def drawImage(self, event, qp, image):
        pixmap = QPixmap(image)
        qp.drawPixmap(event.rect(), pixmap)
        #qp.drawPixmap(QRect(0, 0, 1280, 720), pixmap)


    def drawText(self, event, qp, text):
        qp.setPen(QColor(255, 255, 255))
        qp.setFont(QFont('Consolas', 48))
        qp.drawText(event.rect(), Qt.AlignCenter, text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())