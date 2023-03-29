class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        
        niceSubstr = ""
        
        for windowEnd in range(len(s)):
            
            for windowStart in range(windowEnd+1):
                
                substr = s[windowStart:windowEnd+1]
                
                if self.isNice(substr):
                    niceSubstr = max(niceSubstr, substr, key=len)
        
        return niceSubstr
        
    
    
    def isNice(self, substr):
        
        charFreq = Counter("".join(set(substr)))
        
        for key in charFreq:
            validChar = key.upper() in charFreq and key.lower() in charFreq
            
            if not validChar:
                return False
        
        return True
                

            