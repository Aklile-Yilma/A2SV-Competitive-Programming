class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False
        self.val = 0
        self.sum = 0

class MapSum:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, key: str, val: int) -> None:

        changeVal, prevVal = self.searchWord(key)
        cur = self.root
        for char in key:
            if char not in cur.children:
                cur.children[char] = TrieNode()

            cur = cur.children[char]
            if changeVal:
                cur.sum -= prevVal
            cur.sum += val

        cur.isEnd = True
        cur.val = val

    def sum(self, prefix: str) -> int:
        
        #search prefix
        cur = self.root
        for char in prefix:
            if char not in cur.children:
                return 0
            cur = cur.children[char]

        return cur.sum

    def searchWord(self, word):

        cur = self.root

        for char in word:
            if char not in cur.children:
                return [False, 0]
            cur = cur.children[char]

        return [cur.isEnd, cur.val]

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)