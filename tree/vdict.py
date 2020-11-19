class Vdict(dict):
    '''
    键不存在时自动创建子字典的字典类
    '''

    def __getitem__(self, key):
        # 对于不存在的key,自动在当前位置生成dict
        if not hasattr(self, key):
            self[key] = Vdict()
        return super(Vdict, self).__getitem__(key)
