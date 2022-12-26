class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        #create an empty list
        merged_list = ['']*((len(word1) + len(word2))*2)
        
        
        # insert characters of word1 at even indexes 
        idx = 0
        for char in word1:
            merged_list[idx] = char
            idx += 2
            
        # insert characters of word2 at odd indexes 
        idx = 1
        for char in word2:
            merged_list[idx] = char
            idx += 2
            
        return ''.join(merged_list)
            
        