from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]: 
        
        p_count = Counter(p)
        k = len(p)
        letter_map = {}
        result = []
        left = 0
        
        for right, letter in enumerate(s):
            # add to letter_map
            if letter in p_count.keys():
                
                if letter not in letter_map:
                    letter_map[letter] = 1
                else:
                    letter_map[letter] += 1
            else:
                left = right + 1
                letter_map = {}
                
            # check window
            if right-left+1 == k:
                if p_count == letter_map:
                    result.append(left)
                    
                letter_map[s[left]] -= 1
                if letter_map[s[left]] == 0:
                    del letter_map[s[left]]
                left += 1    
                
        return result
            
            
        
    
        
        
        