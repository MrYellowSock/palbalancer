from Status import IPalStatus
from Element import ElementTable
from PalModule import Pal
from Attack import Attack
from DeriveStatus import AgilityStatus
from Status import PalStatusType
from ElementRelationTable import ElementRelationTable
import numpy as np
class Battle:
    def __init__(self,pal1:Pal,pal2:Pal) -> None:
        self.pals = (pal1,pal2)
        self.status = [dict(),dict()]
        self.applyStatus()
    def applyStatus(self):
        statsLists :tuple[dict[type,list[IPalStatus]]] = ({},{})
        for t1 in self.pals[0].elements:
            for t2 in self.pals[1].elements:
                #Many to Many Elements
                instance = ElementRelationTable.Instance()
                for i in range(2):
                    j = (i+1)%2
                    types = (t1,t2) if i == 0 else (t2,t1)
                    if types in instance.data.keys():
                        for stat in instance.data[types]:
                            if stat.statusType() == PalStatusType.OFFENSIVE:
                                if not stat.type()  in statsLists[i].keys():
                                    statsLists[i][stat.type()]=[]
                                statsLists[i][stat.type()].append(stat)
                            elif stat.statusType() == PalStatusType.DEFENSIVE:
                                if not stat.type()  in statsLists[j].keys():
                                    statsLists[j][stat.type()]=[]
                                statsLists[j][stat.type()].append(stat)
        for i in range(2):
            for t,stats in statsLists[i].items():
                #Combine Same Type
                self.status[i][t] = stats[0].combineMethod().execute(stats)
                #Check empty
                if len(self.status[i]) > 0:
                    #Sort Data By Priority
                    self.status[i] = dict(sorted(self.status[i].items(),key = lambda item:item[1].priority()))
    def execute(self,sampleCount = 1):
        result = 0
        for i in range(2):
            mn,mx = (0,sampleCount//2) if i == 0 else (sampleCount//2,sampleCount)
            for j in range(mn,mx):
                k=j%2
                while self.pals[0].health > 0 and self.pals[1].health>0:
                    attacker,target = self.pals[k],self.pals[1-k]
                    atk = Attack(attacker,target)
                    #Check Status Hit Rate
                    for status in self.status[k].values():
                        status.execute(atk)
                    atk.execute()
                    k=1-k
                if self.pals[0].health >0:
                    result+=1
                self.pals[0].reset()
                self.pals[1].reset()
        
        return result/sampleCount*100
    
          
              
class Composer:
    def __init__(self) -> None:
        pass
    def battle(crt1:Pal,crt2:Pal,amount = 1):
        return Battle(crt1,crt2).execute(amount)
    
    def battleAll(pal:Pal,palList:list[Pal],amount,isPrecise = False):
        if pal is None or palList is None or len(palList) == 0:
            return None
        result = {}
        data = [Composer.battle(pal,pal2,amount) if pal != pal2 else -1 for pal2 in palList]
        data.sort()
        if not isPrecise:
            data.remove(-1)
        length = len(data)

        result['data'] = np.array(data)
        result['mean'] = np.mean(data)
        result['median'] = data[length//2] if len(data)%2 == 1 else (data[length//2]+data[length//2+1])/2
        result['sd'] = np.sqrt(np.var(data))
        return result
                