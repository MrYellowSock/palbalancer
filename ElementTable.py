from Element import IElement
from DeriveElement import *
class ElementTable:
    def instance() -> 'ElementTable': 
        return elementTable
    def __init__(self) -> None:
        self.datas :dict[type,IElement] = {}
    def add(self,element:IElement) :
        self.datas[element.type] = element
    def getElement(self,t:type) -> IElement:
        if t in self.datas.keys():
            return self.datas[t]
        else:
            return None
    def stringToType(self,s:str):
        return next(t for t,element in self.datas.items() if element.name == s)
    
elementTable = ElementTable()
elementTable.add(FireElement())
elementTable.add(WaterElement())
elementTable.add(EarthElement())
elementTable.add(DarkElement())
elementTable.add(IceElement())
elementTable.add(LeafElement())
elementTable.add(NormalElement())
elementTable.add(ElectricityElement())
elementTable.add(DragonElement())