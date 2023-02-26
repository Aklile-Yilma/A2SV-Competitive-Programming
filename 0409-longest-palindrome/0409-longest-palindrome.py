class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        letters_map = {}
        count = 0
        odd = 0
        
        for letter in s:
            if letter in letters_map:
                letters_map[letter] += 1
            else:
                letters_map[letter] = 1
        
        for key in letters_map.keys():
            value = letters_map[key]
            
            if value % 2 == 0:
                count += value
            else:
                odd = 1 # add 1 odd to center
                count += value - 1
                
                
        return count + odd