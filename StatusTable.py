from Status import IPalStatus
from DeriveStatus import *
class StatusTable:
    def instance() -> 'StatusTable': 
        return statusTable
    def __init__(self) -> None:
        self.datas :dict[type,IPalStatus] = {}
    def add(self,status:IPalStatus) :
        self.datas[status.type()] = status
    def InitStatus(self,t:type,val = None) -> IPalStatus:
        if t in self.datas.keys():
            return self.datas[t].clone(val)
        else:
            return None
    def InitStatusByName(self,name,val=None) -> IPalStatus:
        for status in self.datas.values():
            if status.name() == name:
                return status.clone(val)
        return None
statusTable = StatusTable()
statusTable.datas[CriticalStatus]=CriticalStatus()
statusTable.datas[AgilityStatus]=AgilityStatus()