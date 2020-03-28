from PyQt5.QtGui import QPainter, QFont, QColor, QPixmap, QPen, QBrush, QIcon
from PyQt5.QtCore import Qt, QRect, QPoint
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QLabel, \
    QLineEdit, QMainWindow, qApp, QAction, QComboBox, QStyleFactory, QListWidget, QListWidgetItem, \
    QVBoxLayout, QTableWidgetItem, QTableWidget 

    
import sys
import os

class combodemo(QWidget):
    def __init__(self, parent = None):
        super(combodemo, self).__init__(parent)
      
        layout = QHBoxLayout()
        self.cb = QComboBox()
        self.cb.addItem("C")
        self.cb.addItem("C++")
        self.cb.addItems(["Java", "C#", "Python"])
        self.cb.currentIndexChanged.connect(self.selectionchange)
		
        layout.addWidget(self.cb)
        self.setLayout(layout)
        self.setWindowTitle("combo box demo")

    def selectionchange(self,i):
        print("Items in the list are :")
		for count in range(self.cb.count()):
            print(self.cb.itemText(count))
        print ("Current index",i,"selection changed ",self.cb.currentText())

if __name__ == '__main__':
        app = QApplication(sys.argv)
        ex = combodemo()
        ex.show()
        sys.exit(app.exec_())
