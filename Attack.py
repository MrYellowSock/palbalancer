from PalModule import Pal
class Attack :
    def __init__(self,attacker:Pal,target:Pal) -> None:
        self.damage = attacker.atk
        self.attacker: Pal = attacker
        self.target: Pal = target
    def execute(self):
        self.target.health -= self.damage
  