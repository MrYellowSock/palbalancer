from Status import IPalStatus
from Element import IElement,ElementTable
import DeriveStatus

class FireElement(IElement):
    def __init__(self) -> None:
        self.name : str = 'Fire'
        self.effectStatus : dict[type,IPalStatus] = {
            WaterElement : [DeriveStatus.CriticalStatus(10)]
        }
        self.type :type = FireElement
class WaterElement(IElement):
    def __init__(self) -> None:
        self.name : str = 'Water'
        self.effectStatus : dict[type,IPalStatus] = {
            FireElement : 
                [
                    DeriveStatus.CriticalStatus(60),
                    DeriveStatus.AgilityStatus(30)
                ]
        }
        self.type :type = WaterElement

class EarthElement(IElement):
    def __init__(self) -> None:
        self.name : str = 'Earth'
        self.effectStatus : dict[type,IPalStatus] = {
            
        }
        self.type :type = EarthElement
class DarkElement(IElement):
    def __init__(self) -> None:
        self.name : str = 'Dark'
        self.effectStatus : dict[type,IPalStatus] = {
            
        }
        self.type :type = DarkElement
class IceElement(IElement):
    def __init__(self) -> None:
        self.name : str = 'Ice'
        self.effectStatus : dict[type,IPalStatus] = {
            
        }
        self.type :type = IceElement
class LeafElement(IElement):
    def __init__(self) -> None:
        self.name : str = 'Leaf'
        self.effectStatus : dict[type,IPalStatus] = {
            
        }
        self.type :type = LeafElement
class NormalElement(IElement):
    def __init__(self) -> None:
        self.name : str = 'Normal'
        self.effectStatus : dict[type,IPalStatus] = {
            
        }
        self.type :type = NormalElement
class ElectricityElement(IElement):
    def __init__(self) -> None:
        self.name : str = 'Electricity'
        self.effectStatus : dict[type,IPalStatus] = {
            
        }
        self.type :type = ElectricityElement
class DragonElement(IElement):
    def __init__(self) -> None:
        self.name : str = 'Dragon'
        self.effectStatus : dict[type,IPalStatus] = {
            
        }
        self.type :type = DragonElement
def setElementDict():
    table = ElementTable.instance()
    table.add(FireElement())
    table.add(WaterElement())
    table.add(EarthElement())
    table.add(DarkElement())
    table.add(IceElement())
    table.add(LeafElement())
    table.add(NormalElement())
    table.add(ElectricityElement())
    table.add(DragonElement())
    table.sortTable()