import hashlib
import json


class Utils(object):
    '''
    工具类，包括哈希函数
    '''
    @staticmethod
    def hash(block):
        '''
        使用sha256算法得到序列化的区块的哈希
        '''
        block_str = json.dump(block, sort_keys=True)
        return hashlib.sha256(block_str).hexdigest()
