import random
from Status import PalStatusType,IPalStatus,IStatCombineMethod
from Battle import Attack
from DeriveCombineMethod import MaximumStatusCombineMethod
class AgilityStatus(IPalStatus) :
    def __init__(self,val = 0) -> None:
        self.name :str = 'AGI' 
        self.val = val
        self.priority:int = 1
        self.combineMethod : IStatCombineMethod = MaximumStatusCombineMethod()
        self.type:type = AgilityStatus
        self.statusType : PalStatusType = PalStatusType.DEFENSIVE
    def clone(self)->IPalStatus:
        result = AgilityStatus(self.val)
        result.priority = self.priority
        result.combineMethod = self.combineMethod
        result.type = self.type
        result.statusType = self.statusType
        return result
    def execute(self,attack:'Attack') -> None:
        if self.val >= random.randint(0,100):
            attack.damage = 0
class CriticalStatus(IPalStatus) :
    def __init__(self,val = 0) -> None:
        self.name :str = 'CRT' 
        self.val = val
        self.priority:int = 2
        self.combineMethod : IStatCombineMethod = MaximumStatusCombineMethod()
        self.type:type = CriticalStatus
        self.statusType : PalStatusType = PalStatusType.OFFENSIVE
    def clone(self)->IPalStatus:
        result = CriticalStatus(self.val)
        result.priority = self.priority
        result.combineMethod = self.combineMethod
        result.type = self.type
        result.statusType = self.statusType
        return result
    def execute(self,attack:'Attack') -> None:
        if self.val >= random.randint(0,100):
            attack.damage *= 2
