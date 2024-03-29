import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QPushButton, QVBoxLayout, QWidget, QTabWidget,QMessageBox

import pandas as pd
from PyQt5.QtGui import QIcon
from PalModule import Pal
from PalTable import PalTable
from PalElementPowerTable import PalElementPowerTable
from PalMatch import PalMatch
from PalData import PalData
from Element import ElementTable
from ElementRelationTable import ElementRelationTable

class Window(QWidget):
    def __init__(self, pals:list[Pal]):
        QWidget.__init__(self)
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.table = PalTable(pals, 2)
        
        #self.table.onFullChanged(lambda pals: self.showMatch(pals[0],pals[1]))
        self.table.onFullChanged(lambda pal: self.showData(pal[0],pals))
        self.powerTable = PalElementPowerTable(ElementRelationTable.Instance().GetElementRelationDF())
        self.match = None
        
        self.tabwidget = QTabWidget()
        self.tabwidget.addTab(self.table, "Pals")
        self.tabwidget.addTab(self.powerTable, "Elements")
        layout.addWidget(self.tabwidget)
        
    def showMatch(self, pal1: Pal, pal2: Pal):
        # Create a new match widget
        if self.match:
            self.tabwidget.removeTab(2)
            self.match.deleteLater()
        self.match = PalMatch(pal1, pal2)
        self.tabwidget.addTab(self.match, "Match")
    def showData(self,pal1: Pal,pals: list[Pal]):
        if self.match:
            self.tabwidget.removeTab(2)
            self.match.deleteLater()
        self.match = PalData(pal1,pals)
        self.tabwidget.addTab(self.match, "Data")

        

if __name__ == "__main__":
    palTable: pd.DataFrame = pd.read_csv('./resource/PalData.csv')
    # ["Name", "MeleeAttack", "ShotAttack", "HP", "Image"]
    #print( palTable[["ElementType1","ElementType2"]].map(lambda x: x.replace("EPalElementType::","")))
    pals = palTable.apply(lambda row:     
         Pal(
            row["Name"],
            row[["ElementType1","ElementType2"]].map(lambda x: x.replace("EPalElementType::","")).values,
            row[["MeleeAttack","ShotAttack"]].values,
            row["HP"],
            f'./resource/images/{row["Name"]}.png'
        ), axis=1
    )
    app = QApplication(sys.argv)
    screen = Window(pals)
    screen.show()
    sys.exit(app.exec_())
