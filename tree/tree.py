from tree.vdict import Vdict


class Tree(object):
    '''
    索引树，通过嵌套字典实现，包括更新节点和获取节点功能
    '''

    def __init__(self):
        self.tree = Vdict()

    def update(self, hospital: str, department: str, doctor: str, patient: str, pos: tuple):
        self.tree[hospital][department][doctor][patient] = pos

    def get(self, hospital: str, department: str, doctor: str, patient: str):
        '''
        返回结果可能是空dict,也可能是代表位置的tuple
        '''
        return self.tree[hospital][department][doctor][patient]
