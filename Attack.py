from PalModule import Pal
class Attack :
    def __init__(self,attacker,target) -> None:
        self.damage = 1
        self.attacker: Pal = attacker
        self.target: Pal = target
    def execute(self):
        self.target.health -= self.damage
  