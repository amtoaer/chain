from tree.vdict import Vdict


class Tree(object):
    def __init__(self):
        self.tree = Vdict()

    def update(self, hospital: str, department: str, doctor: str, patient: str, pos: tuple):
        self.tree[hospital][department][doctor][patient] = pos

    def get(self, hospital: str, department: str, doctor: str, patient: str):
        # 可能是空dict,也可能是代表位置的tuple
        return self.tree[hospital][department][doctor][patient]
