import sys
from PyQt5 import uic
from PyQt5 import QtCore, QtGui 
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtCore import *
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import sys 

form_class = uic.loadUiType("./ui.ui")[0]


class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.plot([1,2,3,4,5,6,7,8,9], [30,31,40,22,67,12,43,33,54])
    def plot(self, hour, temperature):
        self.graphWidget.plot(hour, temperature)
    def start(self):
        print("시작버튼 눌림")
    
        
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()