import numpy as np
from Element import IElement
from ElementTable import ElementTable
class Pal:
    def __init__(self, name: str, elements: list[str], attacks: list[int],health:int, avatar: str):
        self.name = name
        self.elements_name = elements
        self.elements : set[type] = set()
        #Extract Element From Instance Table
        for t,e in ElementTable.instance().datas.items():
            if e.name in elements:
                self.elements.add(e.type)
        self.atk = np.sum(attacks)
        self.mxHealth = health
        self.health = self.mxHealth
        self.avatar = avatar    
    def reset(self):
        self.health = self.mxHealth