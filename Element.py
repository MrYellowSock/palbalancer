from Status import IPalStatus

class IElement:
    def __init__(self) -> None:
        self.name : str = ''
        self.effectStatus : dict[type,list[IPalStatus]] = {}
        self.type :type = IElement
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
    def sortTable(self):
        for k,element in self.datas.items():
            self.datas[k].effectStatus = dict(sorted(element.effectStatus.items(),key=lambda item:item[0]))
    def getRelationTable(self)->dict[str,list[str]]:
        self.sortTable()
        result = {"Element":[element.name for t,element in self.datas.items()]}
        i=0
        for t1,e1 in self.datas.items():
            column = result[e1.name] = []
            for t2,e2 in self.datas.items():
                if t2 in e1.effectStatus:
                    statusList = e1.effectStatus[t2]
                    column.append(str.join('\n',[(status.name+ " : {:.0f}%".format(status.val)) for status in statusList]) ) 
                else:
                    column.append('-')
        return result
elementTable = ElementTable()