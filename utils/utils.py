import hashlib
import json


class Utils(object):
    '''
    工具类，包括哈希函数
    '''
    @staticmethod
    def hash_object(block) -> str:
        '''
        使用sha256算法得到序列化的区块的哈希
        '''
        block_str = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_str).hexdigest()

    @staticmethod
    def hash_str(string: str) -> str:
        '''
        使用sha256算法哈希字符串
        '''
        return hashlib.sha256(string.encode()).hexdigest()
