from typing import Callable
from PyQt5.QtWidgets import   QWidget, QHBoxLayout,QVBoxLayout,QLabel,QMessageBox
from PyQt5.QtGui import QImage,QPixmap
from PyQt5.QtCore import Qt
import matplotlib.pyplot as plt
from PalModule import Pal
from Battle import Composer
from ElementTable import ElementTable
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from HistrogramWidget import HistogramWidget
import numpy as np
class PalCard(QWidget):
    def __init__(self, pal:Pal):
        super().__init__()
        self.nameLabel = QLabel(pal.name)
        self.hpLabel = QLabel(f"HP: {pal.health}")
        self.elementLabel = QLabel(f"Elements: {','.join([ElementTable.instance().getElement(t).name for t in pal.elements])}")
        self.atkLabel = QLabel(f"ATK: {pal.atk}")
        self.imglabel = QLabel() 
        
        self.imglabel.setPixmap(QPixmap(pal.avatar))

        layout = QVBoxLayout()
        layout.addWidget(self.nameLabel)
        layout.addWidget(self.imglabel)
        layout.addWidget(self.hpLabel)
        layout.addWidget(self.elementLabel)
        layout.addWidget(self.atkLabel)
        self.setLayout(layout)
class PalData(QWidget):
    def __init__(self,pal:Pal,palList:list[Pal]):
        super().__init__()
        layout = QHBoxLayout()
        self.palAcard = PalCard(pal)
        self.benmarkCard = HistogramWidget(Composer.battleAll(pal, palList), name="Pal Win Rate Histogram",xLabel="Win Rate(%)")
        
        layout.addWidget(self.palAcard)
        layout.addWidget(self.benmarkCard)
        self.setLayout(layout)
        
        