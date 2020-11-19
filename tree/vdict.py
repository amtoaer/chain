class Vdict(dict):
    '''
    键不存在时自动创建子字典的字典类
    '''

    def __missing__(self, key):
        value = self[key] = type(self)()
        return value
