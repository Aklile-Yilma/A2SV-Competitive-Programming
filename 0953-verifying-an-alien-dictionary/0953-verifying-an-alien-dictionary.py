class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        
        
        left, right = 0 , 1
        
        while (right < len(words)):
            
            idx = 0
            min_word_len = min(len(words[left]), len(words[right]))
            
            while (idx < min_word_len):
            
                if(idx < min_word_len and order.index(words[left][idx]) < order.index(words[right][idx])):
                    # left += 1
                    # right += 1
                    break

                elif(idx < min_word_len and order.index(words[left][idx]) == order.index(words[right][idx])):
                                        
                    # if((idx == min_word_len -1) and (len(words[left]) == len(words[right]))):
                    #     # if the words are completely equal                         
                    #     return True
                    if((idx == min_word_len - 1)):
                        if(len(words[left]) < len(words[right])): 
                            break
                        elif(len(words[left]) == len(words[right])):
                             # if the words are completely equal        
                            break
                        else:
                             # the word that is at the right is less than in size and equal in order at every character at left index
                            return False
                    else:
                        idx += 1                    

                elif(order.index(words[left][idx]) > order.index(words[right][idx])): 
                    return False

                else:
                    # the word that is at the right is less than in size and equal in order at every character at left index
                    return False
            
            left += 1
            right += 1
                
        return True
                
            
                
            
        
            
            