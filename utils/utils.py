import hashlib
import json


class Utils(object):
    @staticmethod
    def hash(block):
        block_str = json.dump(block, sort_keys=True)
        return hashlib.sha256(block_str).hexdigest()
