class IElement:
    def __init__(self) -> None:
        self.name : str = ''
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
    
elementTable = ElementTable()