from cloneModule import ICloneable
from enum import Enum
from Attack import Attack
class PalStatusType(Enum):
    OFFENSIVE =1,
    DEFENSIVE =2

class IPalStatus(ICloneable) :
    def __init__(self,val:float = 0) -> None:
        self.val :float = val
   
    @staticmethod
    def name()->str:
        pass
    @staticmethod
    def priority()->int:
        pass
    @staticmethod
    def type()->type:
        pass
    @staticmethod
    def statusType()->PalStatusType:
        pass
    @staticmethod
    def combineMethod()->'IStatCombineMethod':
        pass
    
    def clone(self,val = None):
        pass
    def execute(self,attack:Attack) -> None:
        pass

class IStatCombineMethod :
    def execute(arr : list[IPalStatus]) -> IPalStatus:
        pass


    