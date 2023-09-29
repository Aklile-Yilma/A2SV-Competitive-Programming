class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        trie = Trie()
        for word in wordDict:
            trie.insert(word)
            
        ans = []
        n = len(s)
        def backtrack(start, curr_cand):
            #basecase
            nonlocal ans
            if start >= n:
                sol = curr_cand.copy()
                ans.append(" ".join(sol))
                return True
            #for loop
            
            for i in range(start, n):
                word = s[start: i+1]
                if trie.search(word):
                    curr_cand.append(word)
                    backtrack(i+1, curr_cand)
                    curr_cand.pop()
        
        backtrack(0, [])            
        return ans            
        
            
            
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False 
        
        
class Trie:
    
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        
        cur = self.root
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]    
        cur.isEnd = True
        
    def search(self, word):
        
        cur = self.root
        
        for char in word:
            if char not in cur.children:
                return False
            cur = cur.children[char]
            
        return cur.isEnd