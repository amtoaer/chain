from flask import Flask, jsonify, request
from chain.chain import BlockChain
from tree.tree import Tree
import time

app = Flask(__name__)

# 区块链
block_chain = BlockChain()
# 索引树
tree = Tree()


@app.route('/new', methods=['POST'])
def new_transaction():
    '''
    加入新的交易
    '''
    info = request.get_json()
    keys = ['hospital', 'department', 'doctor', 'patient', 'content']

    # 检测参数是否齐全
    if not all(key in info for key in keys):
        return jsonify({'status': 'error', 'message': 'parameter mismatch'}), 400

    # 插入区块链
    pos = block_chain.append_new_transaction(
        info['hospital'], info['department'], info['doctor'], info['patient'], info['content'])

    # 插入索引树
    tree.update(info['hospital'], info['department'],
                info['doctor'], info['patient'], pos)

    return jsonify({'status': 'success', 'message': block_chain.get_latest_transaction()}), 200


@app.route('/search', methods=['POST'])
def search_transaction():
    '''
    通过医院、科室、医生、病人查找交易摘要
    '''
    info = request.get_json()
    keys = ['hospital', 'department', 'doctor', 'patient']
    # 检测参数是否齐全
    if not all(key in info for key in keys):
        return jsonify({'status': 'error', 'message': 'parameter mismatch'}), 400

    # 遍历搜索开始时间
    time_begin = time.time()

    summary_traversal = block_chain.search_transaction(
        info['hospital'], info['department'], info['doctor'], info['patient'])

    # 遍历搜索结束
    time_traversal = time.time()-time_begin

    # 索引树搜索开始时间
    time_begin = time.time()

    summary_index = block_chain.get_transaction(tree.get(
        info['hospital'], info['department'], info['doctor'], info['patient']))

    # 索引树搜索结束
    time_index = time.time()-time_begin

    return jsonify({"status": "success", "message": {
        'time_traversal': time_traversal,
        'summary_traversal': summary_traversal,
        'time_index': time_index,
        'summary_index': summary_index,
    }}), 200
