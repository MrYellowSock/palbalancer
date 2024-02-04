import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QPushButton, QVBoxLayout, QWidget, QTabWidget,QMessageBox
import pandas as pd
from PyQt5.QtGui import QIcon
from Pal import Pal
from PalTable import PalTable
from PalElementPowerTable import PalElementPowerTable
from PalMatch import PalMatch

class Window(QWidget):
    def __init__(self, pals:list[Pal], powerTable: pd.DataFrame):
        QWidget.__init__(self)
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.table = PalTable(pals, 2)
        self.table.onFullChanged(lambda pals: self.showMatch(pals[0],pals[1]))
        self.powerTable = PalElementPowerTable(powerTable)
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

        

if __name__ == "__main__":
    palTable: pd.DataFrame = pd.read_csv('./resource/PalData.csv')
    elementPowerTable = pd.read_csv('./resource/PalElementPower.csv')
    # ["Name", "MeleeAttack", "ShotAttack", "HP", "Image"]
    pals = palTable.apply(lambda row: Pal(row["Name"],
        filter(lambda elem : elem != "None", row[["ElementType1","ElementType2"]].map(lambda x: x.replace("EPalElementType::","")).values) ,
        row[["MeleeAttack","ShotAttack"]].values,
        row["HP"],
        f'./resource/images/{row["Name"]}.png'
    ), axis=1)

    app = QApplication(sys.argv)
    screen = Window(pals,elementPowerTable)
    screen.show()
    sys.exit(app.exec_())
