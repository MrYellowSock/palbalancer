import numpy as np
import random
from Status import PalStatusType,IPalStatus,IStatCombineMethod
from Element import IElement,ElementTable
class Pal:
    def __init__(self, name: str, elements: list[str], attacks: list[int],
                 health: int, avatar: str):
        self.name = name
        self.elements : set[type] = set()
        for t,e in ElementTable.instance().datas.items():
            if e.name in elements:
                self.elements.add(e.type)
        self.atk = np.average(attacks)
        self.mxHealth = 8
        self.health = self.mxHealth
        self.avatar = avatar
        self.defensiveStatus : dict[type,IPalStatus] = {}
        self.offensiveStatus : dict[type,IPalStatus] = {}
    def setStatus(self,t:type,stat:IPalStatus,statusType : PalStatusType):
        if statusType == PalStatusType.DEFENSIVE:
            self.defensiveStatus[t] = stat
        elif statusType == PalStatusType.OFFENSIVE:
            self.offensiveStatus[t] = stat
    def clearStatus(self):
        self.defensiveStatus.clear()
        self.offensiveStatus.clear()
    def resetHealth(self):
        self.health = self.mxHealth
    def reset(self):
        self.clearStatus()
        self.resetHealth()