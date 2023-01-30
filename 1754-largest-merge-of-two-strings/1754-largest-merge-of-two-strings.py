class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        
        first_ptr, second_ptr = 0, 0
        merge = []
        
        while first_ptr < len(word1) and second_ptr < len(word2):
            
            if word1[first_ptr:] > word2[second_ptr:]:
                merge.append(word1[first_ptr])
                first_ptr += 1
                
            else:
                merge.append(word2[second_ptr])
                second_ptr += 1
                
        merge.extend(word1[first_ptr:])
        merge.extend(word2[second_ptr:])
                
        
        return ''.join(merge)
            
            
            
        