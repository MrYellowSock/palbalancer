from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from HistrogramWidget import HistogramWidget
from PalModule import Pal
from Battle import Composer
import numpy as np
class OverallTab(QWidget):
    def __init__(self,pals:list[Pal]) -> None:
        super().__init__()
        sds = []
        means = []
        medians = []
        datas = np.array([])
        for pal in pals:
            data = Composer.battleAll(pal,pals)
            datas = np.concatenate((datas,data),axis=None)
            sds.append(np.std(data))
            means.append(np.mean(data))
            medians.append(np.median(data))
        sds = np.array(sds)
        means = np.array(means)
        medians = np.array(medians)

        layout = QHBoxLayout()
        layout.addWidget(HistogramWidget(datas,name='Winrate Overall'))
        layout.addWidget(HistogramWidget(medians,name='Winrate Overall Median'))
        layout.addWidget(HistogramWidget(means,name='Winrate Overall Mean'))
        layout.addWidget(HistogramWidget(sds,name='Winrate Overall Standard Division'))
        
        self.setLayout(layout)