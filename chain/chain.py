from time import time
from utils.utils import Utils


class BlockChain(object):
    '''
    区块链类，支持加入交易、打包区块、遍历查询交易、通过坐标得到交易
    '''

    def __init__(self):
        # 区块链
        self.blocks = []
        # 当前拥有的交易
        self.transactions = []
        # 加入创世区块
        self.__append_new_block("100")

    def __append_new_block(self, previous_hash: str = ''):
        '''
        将当前所有交易打包成区块
        '''
        self.blocks.append({
            'index': len(self.blocks)+1,
            'timestamp': time(),
            'transactions': self.transactions,
            'previous_hash': previous_hash if previous_hash != '' else Utils.hash_object(self.blocks[-1])
        })
        # 清空当前交易
        self.transactions.clear()

    def append_new_transaction(self, hospital: str, department: str, doctor: str, patient: str, content: str) -> tuple:
        '''
        加入交易，内容分别为（医院，科室，医生，病人，病历摘要）
        '''
        # 每满十笔交易打包一个区块
        if len(self.transactions) == 10:
            self.__append_new_block()

        # 对病历内容进行hash得到摘要
        summary = Utils.hash_str(content)

        # 获取交易插入位置
        pos = (len(self.blocks), len(self.transactions))

        # 插入交易
        self.transactions.append({
            'hospital': hospital,
            'department': department,
            'doctor': doctor,
            'patient': patient,
            'summary': summary,
        })

        # 返回插入位置
        return pos

    def search_transaction(self, hospital: str, department: str, doctor: str, patient: str) -> str:
        '''
        通过医院、科室、医生和病人定位某个交易并得到该次交易摘要（遍历查询）
        '''
        result: str = None
        # 遍历区块
        for block in self.blocks:
            for transaction in block["transactions"]:
                if transaction['hospital'] == hospital and transaction['department'] == department and transaction['doctor'] == doctor and transaction['patient'] == patient:
                    result = transaction['summary']
        # 遍历缓存区
        for transaction in self.transactions:
            if transaction['hospital'] == hospital and transaction['department'] == department and transaction['doctor'] == doctor and transaction['patient'] == patient:
                result = transaction['summary']
        return result

    def get_transaction(self, indexs) -> str:
        '''
        通过某个坐标得到该位置的交易摘要（坐标从索引树中给出）
        '''
        if indexs == {}:
            return None
        block_index, transaction_index = indexs
        # 如果还未打包成区块，则直接从缓存区中取
        if block_index == len(self.blocks):
            return self.transactions[transaction_index]['summary']
        # 否则在区块中取
        return self.blocks[block_index]['transactions'][transaction_index]['summary']
