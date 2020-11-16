from time import time
from utils.utils import Utils


class BlockChain(object):
    def __init__(self):
        # 区块链
        self.blocks = []
        # 当前拥有的交易
        self.transactions = []
        # 加入创世区块
        self.append_new_block("100")

    def append_new_block(self, previous_hash: str = ''):
        # 将当前所有交易打包成区块
        self.blocks.append({
            'index': len(self.blocks)+1,
            'timestamp': time(),
            'transactions': self.transactions,
            'previous_hash': previous_hash if previous_hash != '' else Utils.hash(self.blocks[-1])
        })
        # 清空当前交易
        self.transactions.clear()

    def append_new_transaction(self, hospital: str, department: str, doctor: str, patient: str, summary: str):
        # 加入交易，内容分别为（医院，科室，医生，病人，病历摘要）
        self.transactions.append({
            'hospital': hospital,
            'department': department,
            'doctor': doctor,
            'patient': patient,
            'summary': summary,
        })
