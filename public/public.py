from chain.chain import BlockChain
from tree.tree import Tree
import time


class Public(object):

    def __init__(self):
        # 区块链
        self.block_chain = BlockChain()
        # 索引树
        self.tree = Tree()

    def new_transaction(self, info):
        '''
        加入新的交易
        '''

        # 插入区块链
        pos = self.block_chain.append_new_transaction(
            info['hospital'], info['department'], info['doctor'], info['patient'], info['content'])

        # 插入索引树
        self.tree.update(info['hospital'], info['department'],
                         info['doctor'], info['patient'], pos)

        return self.block_chain.get_latest_transaction()

    def search_transaction(self, info):

        # 遍历搜索开始时间
        time_begin = time.time()

        self.block_chain.search_transaction(
            info['hospital'], info['department'], info['doctor'], info['patient'])

        # 遍历搜索结束
        time_traversal = time.time()-time_begin

        # 索引树搜索开始时间
        time_begin = time.time()

        self.block_chain.get_transaction(self.tree.get(
            info['hospital'], info['department'], info['doctor'], info['patient']))

        # 索引树搜索结束
        time_index = time.time()-time_begin

        return (time_index, time_traversal)
