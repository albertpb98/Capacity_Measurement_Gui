
import sys
import os

from PyQt5.QtGui import QPainter, QFont, QColor, QPixmap, QPen, QBrush, QIcon
from PyQt5.QtCore import Qt, QRect, QPoint
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QLabel, QLineEdit, QMainWindow, qApp, QAction
from hola import ploteoZF, ploteoPhF, ploteoCF, ploteoZ1Z2


class Nanotech(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(1280, 720)
        self.setWindowTitle('PAE Biorobotics')

        btn1 = QPushButton("Measurements - 10 Hz", self)
        btn1.resize(250,40)
        btn1.move(400/2-150/2,200/2-40)
        btn1.clicked.connect(self.buttonClicked)

        btn2 = QPushButton("Measurements - 1 Hz", self)
        btn2.resize(250,40)
        btn2.move(400/2-150/2,200/2)
        btn2.clicked.connect(self.buttonClicked) 

        btn3 = QPushButton("Measurements - 0.1 Hz", self)
        btn3.resize(250,40)
        btn3.move(400/2-150/2,200/2 + 40)
        btn3.clicked.connect(self.buttonClicked)     
    
        self.show()


    def buttonClicked(self,e):
        btn_txt = self.sender().text()
        if btn_txt == "Measurements - 10 Hz":
            ploteoZF(1)
            ploteoPhF(1)
            ploteoZ1Z2(1)
            ploteoCF(1)
        elif btn_txt == "Measurements - 1 Hz":
            ploteoZF(2)
            ploteoPhF(2)
            ploteoZ1Z2(2)
            ploteoCF(2)
        elif btn_txt == "Measurements - 0.1 Hz":
            ploteoZF(3)
            ploteoPhF(3)
            ploteoZ1Z2(3)
            ploteoCF(3)
               

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
            nano = Nanotech()
            nano.show()
            sys.exit(app.exec_())