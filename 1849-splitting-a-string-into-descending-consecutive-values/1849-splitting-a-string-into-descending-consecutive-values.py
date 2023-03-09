class Solution:
    def splitString(self, s: str) -> bool:
        
        def backtrack(start, prev):
            
            if start >= len(s):
                return True
            
            for idx in range(start, len(s)):
                #pruning
                val = int(s[start:idx+1])
                if val + 1 == prev:
                    if backtrack(idx + 1, val):
                        return True
                    
            return False
        
        for idx in range(len(s)-1):
            val = int(s[:idx+1])
            if backtrack(idx+1, val):
                return True
            
        return False
        
        
        
        
        
        