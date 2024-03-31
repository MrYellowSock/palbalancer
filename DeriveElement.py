from Element import IElement

class FireElement(IElement):
    def __init__(self) -> None:
        self.name : str = 'Fire'
        self.type :type = FireElement
class WaterElement(IElement):
    def __init__(self) -> None:
        self.name : str = 'Water'
        self.type :type = WaterElement

class EarthElement(IElement):
    def __init__(self) -> None:
        self.name : str = 'Earth'
        self.type :type = EarthElement
class DarkElement(IElement):
    def __init__(self) -> None:
        self.name : str = 'Dark'
        self.type :type = DarkElement
class IceElement(IElement):
    def __init__(self) -> None:
        self.name : str = 'Ice'
        self.type :type = IceElement
class LeafElement(IElement):
    def __init__(self) -> None:
        self.name : str = 'Leaf'
        self.type :type = LeafElement
class NormalElement(IElement):
    def __init__(self) -> None:
        self.name : str = 'Normal'
        self.type :type = NormalElement
class ElectricityElement(IElement):
    def __init__(self) -> None:
        self.name : str = 'Electricity'
        self.type :type = ElectricityElement
class DragonElement(IElement):
    def __init__(self) -> None:
        self.name : str = 'Dragon'
        self.type :type = DragonElement
