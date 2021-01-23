from chain.chain import BlockChain
from tree.tree import Tree
import time


class Public(object):

    def __init__(self):
        # 区块链
        self.block_chain = BlockChain()
        # 索引树
        self.tree = Tree()

    def clear(self):
        self.__init__()

    def new_transaction(self, info):
        '''
        加入新的交易
        '''
        first_time = time.time()
        # 插入区块链
        pos = self.block_chain.append_new_transaction(
            info['hospital'], info['department'], info['doctor'], info['patient'], info['content'])
        second_time = time.time()
        # 插入索引树
        self.tree.update(info['hospital'], info['department'],
                         info['doctor'], info['patient'], pos)
        third_time = time.time()
        # 返回插入链时间和更新索引时间
        return second_time-first_time, third_time-second_time

    def search_transaction(self, info):

        # 遍历搜索开始时间
        first_time = time.time()

        self.block_chain.search_transaction(
            info['hospital'], info['department'], info['doctor'], info['patient'])

        # 遍历搜索结束
        second_time = time.time()

        self.block_chain.get_transaction(self.tree.get(
            info['hospital'], info['department'], info['doctor'], info['patient']))

        # 索引树搜索结束
        third_time = time.time()
        # 返回遍历搜索所需时间和索引树搜索所需时间
        return second_time-first_time, third_time-second_time
