import hashlib
import datetime

# each node in linked list
class Block:

    def __init__(self, timestamp, data, previous_hash):
      self.timestamp = timestamp
      self.data = data
      self.previous_hash = previous_hash
      self.hash = self.calc_hash()

    def calc_hash(self):
      sha = hashlib.sha256()
      data_string = str(self.data) + "_" + str(self.timestamp)
      hash_str = data_string.encode("utf-8") # must add encode or you will get TypeError: Unicode-objects must be encoded before hashing
      sha.update(hash_str)
      return sha.hexdigest()

# the linked list
class BlockChain:
    def __init__(self):
        self.current = None

    def add(self, data):

        if (data is None):
            print("Must add valid data to blockchain.")
            return
        
        if (data == ""):
            print("Cannot add empty strings as data to blockchain.")
            return

        # add new block link
        timestamp = datetime.datetime.now()

        # figure out current block and set that as the previous block
        if (self.current is None):
            previous = 0
        else:
            previous = self.current.hash

        # set new current block
        self.current = Block(timestamp, data, previous)

    def get_current_info(self):
        if (self.current is None):
            return "No blocks in blockchain yet"
        else:
            return f"Timestamp: {self.current.timestamp}, Data: {self.current.data}, Previous Hash: {self.current.previous_hash}"

# case 1
chain = BlockChain()
print(chain.get_current_info()) # No blocks in blockchain yet
chain.add("first piece of data")
print(chain.get_current_info())
chain.add("second")
print(chain.get_current_info())
chain.add(3)

# case 2 - adding blocks with None
chain_2 = BlockChain()
chain_2.add(None) # Must add valid data to blockchain.

# case 3 - adding empty string
chain_3 = BlockChain()
chain_3.add("") # Cannot add empty strings as data to blockchain.



