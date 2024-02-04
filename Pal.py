import numpy as np


class Pal:
    def __init__(self, name: str, elements: list[str], attacks: list[int],
                 hp: int, avatar: str):
        self.name = name
        self.elements = set(elements)
        self.atk = np.average(attacks)
        self.hp = hp
        self.avatar = avatar
