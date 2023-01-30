class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        
        first_ptr, second_ptr = 0, 0
        merge = []
        
        while first_ptr < len(word1) and second_ptr < len(word2):
            
            # if two characters are the same pick the lexicographically largest merge
            # that is why we compare with the split operator[:]
            if word1[first_ptr:] > word2[second_ptr:]:
                merge.append(word1[first_ptr])
                first_ptr += 1
                
            else:
                merge.append(word2[second_ptr])
                second_ptr += 1
                
        merge.extend(word1[first_ptr:])
        merge.extend(word2[second_ptr:])
                
        
        return ''.join(merge)
            
            
            
        