class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        abbb
        """
        max_len = 0
        
        for idx in range(26):
            letter = chr(ord('A') + idx)
            curr_k = k
            
            left = 0
            for right in range(len(s)):
                
                if s[right] != letter and curr_k:
                    curr_k-= 1
                elif s[right] != letter:
                    while s[left] == letter:
                        left += 1
                    left += 1
                max_len = max(max_len, right-left+1)
                    
        return max_len
            
        
                    
                
                
            
                
            
        
        