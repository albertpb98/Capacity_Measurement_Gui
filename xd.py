import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QSizePolicy, QWidget, QComboBox, QLabel, QRadioButton, QCheckBox, QGridLayout, QLineEdit
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib as mpl
import matplotlib.pyplot as plt
import random
import numpy as np

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.left = 0
        self.top = 800
        self.title = 'Chip2 Torque Data'
        self.width = 800
        self.height =800
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        l = QGridLayout(self)
        #hbox = MyMplCanvas(self.main_widget, width=50, height=40, dpi=100)
        self.figure = plt.figure(figsize=(15,5))    
        self.canvas = FigureCanvas(self.figure)   
        l.addWidget(self.canvas, 0,0,9,(100-4))

        xselect=QRadioButton("X",self)
        xselect.setChecked(True)

        zselect=QRadioButton("Z",self)

        sselect=QRadioButton("SP1",self)
        l.addWidget(xselect,0,(100-1))
        l.addWidget(zselect,0,(100-2))
        l.addWidget(sselect,0,(100-3))


        pass_list=QComboBox(self)
        pass_list.addItems(sheets_idealcut)
        l.addWidget(pass_list,1,(100-3),1,3)

        rawdata_check=QCheckBox("Raw Data",self)
        rawdata_check.setChecked(True)
        l.addWidget(rawdata_check,2,(100-3),1,3)

        mvgavg_check=QCheckBox("Moving average",self)
        mvgavg_check.setChecked(True)

        mvgstd_check=QCheckBox("Moving stdev",self)
        mvgstd_check.setChecked(True)
        l.addWidget(mvgavg_check,3,(100-3),1,3)
        l.addWidget(mvgstd_check,4,(100-3),1,3)


        xlim_left=QLineEdit("None",self)
        xlim_right=QLineEdit("None",self)

        ylim_top=QLineEdit("None",self)
        ylim_top.textChanged.connect(self.plot)
        ylim_bottom=QLineEdit("None",self)
        ylim_bottom.textChanged.connect(self.plot)

        xlim_left_label=QLabel("X min",self)
        xlim_right_label=QLabel("X max",self)

        ylim_top_label=QLabel("Y max",self)

        ylim_bottom_label=QLabel("Y min",self)
        l.addWidget(xlim_right_label,5,(100-3),1,1)
        l.addWidget(xlim_right,5,(100-2),1,2)
        l.addWidget(xlim_left_label,6,(100-3),1,1)
        l.addWidget(xlim_left,6,(100-2),1,2)

        l.addWidget(ylim_top_label,7,(100-3),1,1)
        l.addWidget(ylim_top,7,(100-2),1,2)
        l.addWidget(ylim_bottom_label,8,(100-3),1,1)
        l.addWidget(ylim_bottom,8,(100-2),1,2)
        self.compute_initial_figure()
        self.show()

    def compute_initial_figure(self):
            axes=self.figure.add_subplot(111)
            t = np.arange(0.0, 3.0, 0.01)
            s = np.sin(2*np.pi*t)
            axes.plot(t, s)
            self.canvas.draw()
            #axes.set_ylim(top=self.ylim_top.text(),bottom=self.ylim_bottom.text()) 
    def plot(self):
            plt.cla()
            axes=self.figure.add_subplot(111)
            t = np.arange(0.0, 3.0, 0.01)
            s = np.sin(2*np.pi*t)
            axes.plot(t, s)
            axes.set_ylim(top=float(self.ylim_top.text()),bottom=float(self.ylim_bottom.text())) 
            self.canvas.draw()

if __name__ == '__main__':
    sheets_idealcut=['pass2','pass3','pass4','pass5']

    app = QApplication(sys.argv)
    w = App()
    app.exec_()