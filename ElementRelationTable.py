from Element import IElement,ElementTable
from Status import IPalStatus
import pandas as pd
from pandas import DataFrame
import DeriveStatus as ds
import DeriveElement as de
import re
from StatusTable import StatusTable
class ElementRelationTable:
    def __init__(self) -> None:
        self.data:dict[tuple[type,type],list[IPalStatus]] = dict()
    def add(self,attackType:type,targetType:type,status:IPalStatus):
        if not (attackType,targetType) in self.data.keys():
            self.data[(attackType,targetType)] = []
        self.data[(attackType,targetType)].append(status)
    def setRelation(self,attackType:type,targetType:type,statusList:list[IPalStatus]):
        self.data[(attackType,targetType)] = []
        for status in statusList:
            self.add(attackType,targetType,status)
    def Instance() ->'ElementRelationTable':
        return elementTable
    def GetElementRelationDF(self)->pd.DataFrame:
        result = {}
        for t1,element1 in ElementTable.instance().datas.items():
            result[element1.name]=[]
            for t2,element2 in ElementTable.instance().datas.items():
                if (t2,t1) in self.data.keys():
                    result[element1.name].append(",\n".join([f"{type(status).name()} : {status.val:.2f}%" for status in self.data[(t2,t1)]]))
                else:
                    result[element1.name].append('-')
        df = pd.DataFrame(result,
                          index = [element.name for element in ElementTable.instance().datas.values()])
        return df
    def WriteCSV(self):
        self.GetElementRelationDF().to_csv('./resource/ElementRelationTable.csv')
    def ReadCSV(self):
        df:DataFrame = pd.read_csv('./resource/ElementRelationTable.csv')
        df.index = pd.Index( list(df.columns)[1:])
        self.data.clear()
        for t1,e1 in ElementTable.instance().datas.items():
            for t2,e2 in ElementTable.instance().datas.items():
                s = df.loc[e1.name,e2.name]
                for status in self.toStatusList(s):
                    self.add(t1,t2,status)
    @staticmethod
    def toStatusList(s:str) -> list[IPalStatus]:
        if re.match('-',s) is not None:
            return []
        stats = s.replace('\n','').split(",")
        result:list[IPalStatus] = []
        for s in stats:
            match = re.match("\s*(\S*)\s*:\s*(\S*)%\s*", s)
            if match != None:
                status = StatusTable.instance().InitStatusByName(match.group(1),float(match.group(2)))
                if status:
                    result.append(status)
            else :
                return None
        return result
elementTable = ElementRelationTable()
ElementRelationTable.Instance().ReadCSV()
ElementRelationTable.Instance().WriteCSV()