class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        idx_s = 0
        
        for char_t in t:
            if idx_s < len(s) and s[idx_s] == char_t:
                idx_s += 1
                
        return True if idx_s == len(s) else False
                
        