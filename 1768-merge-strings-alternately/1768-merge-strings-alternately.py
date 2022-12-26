class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        merged_list = ['']*((len(word1) + len(word2))*2)
        
        print(merged_list)
        idx = 0
        for char in word1:
            merged_list[idx] = char
            idx += 2
            
        idx = 1
        for char in word2:
            merged_list[idx] = char
            idx += 2
            
        return ''.join(merged_list)
            
        