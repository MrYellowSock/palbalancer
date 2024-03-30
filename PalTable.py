from typing import Callable
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QCheckBox, QWidget
from PyQt5.QtGui import QIcon
from numpy.lib import math
from PalModule import Pal
from PyQt5.QtCore import Qt
from Element import ElementTable
class PalCell(QTableWidgetItem):
    def __init__(self, pal: Pal, onStateChanged: Callable[[bool,Pal],None]):
        super().__init__()
        elements = ','.join([ElementTable.instance().getElement(t).name for t in pal.elements]) 
        self.pal = pal
        self.onStateChanged = onStateChanged 
        self.setText(f"{pal.name}\n[{elements}]")  # Display name and elements in separate lines
        self.setIcon(QIcon(pal.avatar))
        
class PalTable(QTableWidget):
    def __init__(self, pals: list[Pal],colsize: int = 10):
        super().__init__()
        self.onFull = None
        self.setColumnCount(colsize)
        rowsize = math.ceil(len(pals)/colsize)
        self.setRowCount(rowsize)
        self.setEditTriggers(QTableWidget.NoEditTriggers)
        palIndex = 0
        for row in range(rowsize):
            for col in range(colsize):
                if palIndex >= len(pals):
                    break
                palNow = pals[palIndex]
                item = PalCell(palNow,self.updateSelected)
                self.setItem(row, col, item)

                palIndex += 1
        self.cellClicked.connect(lambda row,col: self.updateSelected(self.item(row,col).pal))

        for row in range(self.rowCount()):
            self.setRowHeight(row, 60)  # Set the row height as per your requirement
        for col in range(self.columnCount()):
            self.setColumnWidth(col, 120)
    
    def onFullChanged(self,func: Callable[[Pal],None]):
        self.onFull = func

    def updateSelected(self, pal: Pal):
        if pal and self.onFull != None:
            self.onFull(pal)