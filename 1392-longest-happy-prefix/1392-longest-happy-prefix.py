class Solution:
    def longestPrefix(self, s: str) -> str:

        rev_s = s[::-1]
        LPS = self.buildLPS(rev_s)
        
        ans = ""
        
        for i in range(LPS[-1]):
            ans += s[i]
            
        return ans
        
    def buildLPS(self, pattern):
        
        prev = 0
        i = 1
        m = len(pattern)
        LPS = [0] * m
        
        while i < m:
            if pattern[i] == pattern[prev]:
                LPS[i] = 1 + prev
                prev += 1
                i += 1
            else:
                if prev == 0:
                    i += 1
                else:
                    prev = LPS[prev - 1]
                    
        return LPS