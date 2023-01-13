class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        
        count = 0
        row_length = len(strs)
        col_length = len(strs[0])
        
        
        for col_idx in range(col_length):
            word = ''
            for row_idx in range(row_length):
                word += strs[row_idx][col_idx]
                            
            if not self.isAlphabeticalOrder(word):
                count += 1
                
        return count
            
        
    def isAlphabeticalOrder(self, word):
        return word == ''.join(sorted(word))
                
                
                
                
                
        
        
    
        