from Status import IPalStatus
import DeriveStatus
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
        print(name)
        for status in self.datas.values():
            print('---')
            print(status.name(),name)
            if status.name() == name:
                print("Match")
                return status.clone(val)
        return None
statusTable = StatusTable()
statusTable.datas[DeriveStatus.CriticalStatus]=DeriveStatus.CriticalStatus()
statusTable.datas[DeriveStatus.AgilityStatus]=DeriveStatus.AgilityStatus()