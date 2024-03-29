import random
from Status import PalStatusType,IPalStatus,IStatCombineMethod
from Attack import Attack
from DeriveCombineMethod import MaximumStatusCombineMethod
class AgilityStatus(IPalStatus) :
    def __init__(self,val = 0) -> None:
        self.val = val
    @staticmethod
    def name()->str:
        return 'AGI'
    @staticmethod
    def priority()->int:
        return 1
    @staticmethod
    def type()->type:
        return AgilityStatus
    @staticmethod
    def statusType()->PalStatusType:
        return PalStatusType.DEFENSIVE
    @staticmethod
    def combineMethod()->IStatCombineMethod:
        return MaximumStatusCombineMethod()

    def clone(self,val=None)->IPalStatus:
        result = AgilityStatus(self.val if val is None else val) 
        return result
    def execute(self,attack:'Attack') -> None:
        if self.val >= random.randint(0,100):
            #print("Activate")
            attack.damage = 0
        #else:
            #print("Fail")
class CriticalStatus(IPalStatus) :
    def __init__(self,val = 0) -> None:
        self.val = val
    @staticmethod
    def name()->str:
        return 'CRT' 
    @staticmethod
    def priority()->int:
        return 2
    @staticmethod
    def type()->type:
        return CriticalStatus
    @staticmethod
    def statusType()->PalStatusType:
        return PalStatusType.OFFENSIVE
    @staticmethod
    def combineMethod()->IStatCombineMethod:
        return MaximumStatusCombineMethod()
    
    def clone(self,val = None)->IPalStatus:
        result = CriticalStatus(self.val if val is None else val)
        return result
    def execute(self,attack:'Attack') -> None:
        if self.val >= random.randint(0,100):
            attack.damage *= 2
