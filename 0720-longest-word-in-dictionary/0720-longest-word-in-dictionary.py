class Solution:
    def longestWord(self, words: List[str]) -> str:
        
        trie = Trie()
        res = ""
        words.sort()
        for word in words:
            trie.insert(word)
         
        for word in words:
            isValid = trie.isValid(word)
            if isValid and len(word) > len(res):
                res = word
        return res
        

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:
        curr = self.root
        for ch in word:
            if  not ch in curr.children:
                nwNode = TrieNode()
                curr.children[ch] = nwNode
            curr = curr.children[ch]
        curr.isEnd = True
        
    def isValid(self, word):
        curr = self.root
        for ch in word:
            if not curr.children[ch].isEnd:
                return False
            curr = curr.children[ch]            
        return True