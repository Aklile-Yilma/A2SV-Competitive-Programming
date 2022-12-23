# class Solution:
#     def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        
#         left, right = 0 , 1
        
#         while (right < len(words)):
            
#             idx = 0
#             min_word_len = min(len(words[left]), len(words[right]))
            
#             while (idx < min_word_len):
            
#                 if(idx < min_word_len and order.index(words[left][idx]) < order.index(words[right][idx])):
#                     break

#                 elif(idx < min_word_len and order.index(words[left][idx]) == order.index(words[right][idx])):
                                        
#                     if((idx == min_word_len - 1)):
#                         if(len(words[left]) < len(words[right])): 
#                             # if the word at left is equal and less than the word at right
#                             break
#                         elif(len(words[left]) == len(words[right])):
#                              # if the words are completely equal        
#                             break
#                         else:
#                              # the word that is at the right is less than in size and equal in order at every character at left index
#                             return False
#                     else:
#                         idx += 1                    

#                 elif(order.index(words[left][idx]) > order.index(words[right][idx])): 
#                     return False

#                 else:
#                     # the word that is at the right is less than in size and equal in order at every character at left index
#                     return False
            
#             left += 1
#             right += 1
                
#         return True
                
            
                
            
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        alienOrder = {}
        
        # map each char in the alien dictionary to its position
        for index, char in enumerate(order):
            alienOrder[char] = index
            
        
        left, right = 0 , 1
        
        while (right < len(words)):
            
            idx = 0
            min_word_len = min(len(words[left]), len(words[right]))
            
            while (idx < min_word_len):
            
                if(idx < min_word_len and alienOrder[words[left][idx]] < alienOrder[words[right][idx]]):
                    break

                elif(idx < min_word_len and alienOrder[words[left][idx]] == alienOrder[words[right][idx]]):
                                        
                    if((idx == min_word_len - 1)):
                        if(len(words[left]) < len(words[right])): 
                            # if the word at left is equal and less than the word at right
                            break
                        elif(len(words[left]) == len(words[right])):
                             # if the words are completely equal        
                            break
                        else:
                             # the word that is at the right is less than in size and equal in order at every character at left index
                            return False
                    else:
                        idx += 1                    

                elif(alienOrder[words[left][idx]] > alienOrder[words[right][idx]]): 
                    return False

                else:
                    # the word that is at the right is less than in size and equal in order at every character at left index
                    return False
            
            left += 1
            right += 1
            
        return True
                
        
            
            