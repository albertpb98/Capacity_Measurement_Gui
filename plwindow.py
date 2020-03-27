

import sys
import os

from hola import ploteo
from PyQt5.QtGui import QPainter, QFont, QColor, QPixmap, QPen, QBrush, QIcon
from PyQt5.QtCore import Qt, QRect, QPoint
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QLabel, \
    QLineEdit, QMainWindow, qApp, QAction, QComboBox, QStyleFactory, QListWidget, QListWidgetItem, \
    QVBoxLayout, QTableWidgetItem, QTableWidget    



class Plotis(QWidget):
    def __init__(self, parent = None):
        super(Plotis,self).__init__(parent)
        #QApplication.setStyle(QStyleFactory.create('0.1 Hz'))
        #QApplication.setStyle()
        samplesList = ["MM", "M1", "M2"]

        #Create the QCOMBOBOX
        cbx = QComboBox()   #Adds items in a list object
        cbx.addItems(samplesList)   #Answer the text event change
        item = cbx.currentText()    #Retrieves the text of currently selected item

        #QLISTWIDGET
        items = ['Z(f)','C(f)', 'Z2(Z1)', 'Ph(f)']

        self.lv = QListWidget()
        self.lv.addItems(items)
        self.lv.itemSelectionChanged.connect(self.itemChanged)

        vbx = QVBoxLayout()
        vbx.setAlignment(Qt.AlignTop)
        vbx.addWidget(cbx)
        vbx.addWidget(self.lv)

        self.resize(500, 350)
        self.setWindowTitle('Choose the sample to measure')
        self.setLayout(vbx)


    def clikedItem(self,item):
        if item == "MM":
            items = ['Z(f)','C(f)', 'Z2(Z1)', 'Ph(f)']
        elif item == "M1":
            items = ['Z(f)','C(f)', 'Z2(Z1)', 'xD(f)']
        elif item == "M2":
            items = ['Z(f)','C(f)', 'Z2(Z1)', 'Ph(f)']
        return items

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

    def textChanged(self,txt):
        QApplication.setStyle(QStyleFactory.create(txt))

    def itemChanged(self):
        item = QListWidgetItem(self.lv.currentItem())
        print("Chosen system:", item.text)            

if __name__ == '__main__':
    app = QApplication(sys.argv)
    pl = Plotis()
    pl.show()
    sys.exit(app.exec_())