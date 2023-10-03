class TrieNode:

    def __init__(self) -> None:
        self.is_end = False
        self.children = {}

        
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        cur = self.root
        word = word.lower()
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode(); 
            cur = cur.children[char]

        cur.is_end = True
        

    def search(self, word: str) -> bool:
        
        n = len(word)
        
        def helper(cur, idx):
            if idx >= n:
                return cur.is_end
            
            char = word[idx]
            opt1, opt2 = False, False
            if char != '.':
                if char in cur.children:
                    opt1 = helper(cur.children[char], idx+1)
                if opt1:
                    return True
                
            else:
                for char in cur.children:
                    opt2 = helper(cur.children[char], idx+1)
                    if opt2:
                        return True
                    
            return opt1 or opt2
                
                
        return helper(self.root, 0)
    

        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)