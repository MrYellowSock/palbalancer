from cloneModule import ICloneable
from enum import Enum
class PalStatusType(Enum):
    OFFENSIVE =1,
    DEFENSIVE =2

class IPalStatus(ICloneable) :
    def __init__(self,val:float = 0) -> None:
        self.name :str = '' 
        self.val :float = val
        self.priority:int = 0
        self.combineMethod : IStatCombineMethod
        self.type:type 
        self.statusType : PalStatusType 
    def clone(self):
        pass
    def execute(self,attack:'Attack') -> None:
        pass

class IStatCombineMethod :
    def execute(arr : list[IPalStatus]) -> IPalStatus:
        pass
    