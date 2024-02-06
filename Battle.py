from Status import IPalStatus
from Element import ElementTable
from PalModule import Pal
class Attack :
    def __init__(self,attacker,target) -> None:
        self.damage = 1
        self.attacker: Pal = attacker
        self.target: Pal = target
    def execute(self):
        statusList = list(self.target.defensiveStatus.values()) + list(self.attacker.offensiveStatus.values())
        statusList.sort(key=lambda status:status.priority)
        for status in statusList:
            status.execute(self)
        self.target.health -= self.damage
        #print(self.attacker.name,'attack',self.target.name,'with damage',self.damage,self.target.name,'Health :',self.target.health)

class Composer:
    def __init__(self) -> None:
        pass
    def battle(crt1:Pal,crt2:Pal,amount = 1):
        Composer.applyStatus(crt1,crt2)
        sortFunc = lambda item:item[1].priority
        crt1.defensiveStatus = dict(sorted(crt1.defensiveStatus.items(),key= sortFunc)) 
        crt2.defensiveStatus = dict(sorted(crt2.defensiveStatus.items(),key= sortFunc)) 
        crt1.offensiveStatus = dict(sorted(crt1.offensiveStatus.items(),key= sortFunc)) 
        crt2.offensiveStatus = dict(sorted(crt2.offensiveStatus.items(),key= sortFunc)) 
        result = 1
        state = False
        attacker = crt1
        target = crt2
        firstPal = crt1
        for i in range(amount):
            if not state and i>amount//2:
                state = True
                attacker,target  = target,attacker
            while crt1.health >0 and crt2.health>0:
                atk = Attack(attacker,target)
                atk.execute()
                attacker,target = target,attacker
            if firstPal.health>0:
                result+=1
            crt1.resetHealth()
            crt2.resetHealth()
        crt1.reset()
        crt2.reset()
        return result/amount*100
    def applyStatus(crt1:Pal,crt2:Pal):
        stats1 :dict[type,list[IPalStatus]] = {}
        stats2 :dict[type,list[IPalStatus]] = {}
        for t1 in crt1.elements:
            for t2 in crt2.elements:
                table = ElementTable.instance()
                e1 =table.getElement(t1)
                if t2 in e1.effectStatus.keys():
                    statusList = e1.effectStatus[t2]
                    for stat in statusList:
                        if stat.type in stats1:
                            stats1[stat.type].append(stat)
                        else:
                            stats1[stat.type] = [stat]
                e2 =table.getElement(t2)
                if t1 in e2.effectStatus.keys():
                    statusList = e2.effectStatus[t1]
                    for stat in statusList:
                        if stat.type in stats2 :
                            stats2[stat.type].append(stat)
                        else :
                            stats2[stat.type] = [stat]
        for t,statList in stats1.items():
            stat:IPalStatus = statList[0].combineMethod.execute(list(statList))
            crt1.setStatus(t,stat,stat.statusType)
        for t,statList in stats2.items():
            stat = statList[0].combineMethod.execute(list(statList))
            crt2.setStatus(t,stat,stat.statusType)
