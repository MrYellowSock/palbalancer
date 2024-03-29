from typing import Callable
from PyQt5.QtWidgets import  QTableWidget, QTableWidgetItem, QCheckBox, QWidget, QHBoxLayout,QVBoxLayout,QLabel,QMessageBox
from PyQt5.QtGui import QImage,QPixmap
from numpy.lib import math
from PalModule import Pal
from PyQt5.QtCore import Qt
from Battle import Composer
from Element import ElementTable
class PalCard(QWidget):
    def __init__(self, pal:Pal):
        super().__init__()
        self.nameLabel = QLabel(pal.name)
        self.hpLabel = QLabel(f"HP: {pal.health}")
        self.elementLabel = QLabel(f"Elements: {','.join([ElementTable.instance().getElement(t).name for t in pal.elements])}")
        self.atkLabel = QLabel(f"ATK: {pal.atk}")
        

        self.imglabel = QLabel() 
        pixmap = QPixmap(pal.avatar)
        self.imglabel.setPixmap(pixmap)

        layout = QVBoxLayout()
        layout.addWidget(self.nameLabel)
        layout.addWidget(self.imglabel)
        layout.addWidget(self.hpLabel)
        layout.addWidget(self.elementLabel)
        layout.addWidget(self.atkLabel)
        self.setLayout(layout)

class PalMatch(QWidget):
    def __init__(self,palA:Pal,palB:Pal):
        super().__init__()
        layout = QHBoxLayout()
        self.palAcard = PalCard(palA)
        self.palBcard = PalCard(palB)
        self.matchSummary = QLabel("Win rate "+str(Composer.battle(palA,palB,1000))+"%")

        layout.addWidget(self.palAcard)
        layout.addWidget(self.palBcard)
        layout.addWidget(self.matchSummary)
        self.setLayout(layout)
        
        