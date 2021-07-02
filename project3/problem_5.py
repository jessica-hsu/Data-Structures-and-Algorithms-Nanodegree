## Represents a single node in the Trie
class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.children = {}
        self.word_end = False
    
    def insert(self, char):
        ## Add a child node in this Trie
        self.children[char] = TrieNode()

    def suffixes(self, suffix = ''):
        ## Recursive function that collects the suffix for 
        ## all complete words below this point
        #print(f"find all matches for: {suffix}")
        all_matches = []
        if (self.word_end is True):
            #print("base case")
            all_matches.append(suffix) # found a valid word. add to matches array
        # go through all the children
        for item in self.children.items(): # will return (char, TrieNode)
            prefix = suffix + item[0]
            node = item[1]
            #print(node)
            all_matches += node.suffixes(prefix)

        return all_matches

## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.root = TrieNode()

    def insert(self, word):
        ## Add a word to the Trie
        current = self.root
        for letter in word:
            if (letter not in current.children):
                current.insert(letter) # make a trienode for each letter
            current = current.children[letter] # go deeper
        current.word_end = True # end of word. mark word_end as True

    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        current = self.root
        for letter in prefix:
            if (letter not in current.children):
                return None
            current = current.children[letter]
        #print(type(current))
        return current

    def find_match(self, prefix):
        print(f"finding matches for: {prefix}")
        if (prefix is None):
            print("Please enter a valid input")
            return
        trie = self.find(prefix)
        if (trie is None):
            print([]) # no matches
        else:
            m = trie.suffixes(prefix)
            print(m)


word_list = ['apple', 'bear', 'goo', 'good', 'goodbye', 'goods', 'goodwill', 'gooses'  ,'zebra', "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"]
word_trie = Trie()

# Add words
for word in word_list:
    word_trie.insert(word)

# test case 1
word_trie.find_match("goo") # ['goo', 'good', 'goodbye', 'goods', 'goodwill', 'gooses']

# test case 2
word_trie.find_match("an") # ['ant', 'anthology', 'antagonist', 'antonym']

# test case 3
word_trie.find_match("fac") # ['factory']

# edge case 1: no matches
word_trie.find_match("mug") # []

# edge case 2: show all results
word_trie.find_match("") # ['apple', 'ant', 'anthology', 'antagonist', 'antonym', 'bear', 'goo', 'good', 'goodbye', 'goods', 'goodwill', 'gooses', 'zebra', 'fun', 'function', 'factory', 'trie', 'trigger', 'trigonometry', 'tripod']

# edge case 3: None input
word_trie.find_match(None) # Please enter a valid input