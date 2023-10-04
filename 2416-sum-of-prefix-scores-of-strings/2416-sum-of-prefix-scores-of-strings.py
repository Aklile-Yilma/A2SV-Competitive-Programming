class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        
        
        trie = Trie()
        
        for word in words:
            trie.insert(word)
            
        ans = []
        
        for word in words:
            ans.append(trie.searchPrefix(word)[1])
            
        return ans
        
        
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = True
        self.count = 0
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
        
    def insert(self, word):
        
        cur = self.root
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
                
            cur = cur.children[char]
            cur.count += 1
            
        cur.isEnd = True
        
    def searchPrefix(self, prefix):
        
        cur = self.root
        total = 0
        for char in prefix:
            if char not in cur.children:
                return [False, 0]
            cur = cur.children[char]
            total += cur.count
        
        
        return [True, total]