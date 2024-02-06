from typing import Callable
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QCheckBox
from PyQt5.QtGui import QIcon
from numpy.lib import math
from PalModule import Pal
from PyQt5.QtCore import Qt
from Element import ElementTable
class PalCell(QCheckBox):
    def __init__(self, pal: Pal, onStateChanged: Callable[[bool,Pal],None]):
        super().__init__()
        elements = ','.join([ElementTable.instance().getElement(t).name for t in pal.elements]) 
        self.stateChanged.connect(lambda : onStateChanged(self.isChecked(),pal))
        self.setText(f"{pal.name}\n[{elements}]")  # Display name and elements in separate lines
        self.setIcon(QIcon(pal.avatar))

class PalTable(QTableWidget):
    def __init__(self, pals: list[Pal],maxSelect=2,colsize: int = 10):
        super().__init__()
        self.onFull = None
        self.selecteds = []
        self.maxSelect = maxSelect
        self.setColumnCount(colsize)
        rowsize = math.ceil(len(pals)/colsize)
        self.setRowCount(rowsize)

        palIndex = 0
        for row in range(rowsize):
            for col in range(colsize):
                if palIndex >= len(pals):
                    break
                palNow = pals[palIndex]
                item = PalCell(palNow,self.updateSelected)
                self.setCellWidget(row, col, item)

                palIndex += 1

        for row in range(self.rowCount()):
            self.setRowHeight(row, 60)  # Set the row height as per your requirement
        for col in range(self.columnCount()):
            self.setColumnWidth(col, 120)

    def isFull(self):
        return len(self.selecteds) >= self.maxSelect
    
    def onFullChanged(self,func: Callable[[list[Pal]],None]):
        self.onFull = func

    def updateSelected(self,state, pal: Pal):
        if state:
            self.selecteds.append(pal)
        else:
            self.selecteds.remove(pal)
        for row in range(self.rowCount()):
            for col in range(self.columnCount()):
                item = self.cellWidget(row, col)
                if isinstance(item,PalCell):
                    if self.isFull() and not item.isChecked():
                        item.setEnabled(False)
                    else:
                        item.setEnabled(True)
        if self.isFull() and self.onFull != None:
            self.onFull(self.selecteds)