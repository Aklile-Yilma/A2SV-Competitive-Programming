class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
#         needle_map = Counter(needle)
#         window_map = {}
#         left = 0
        
#         for right in range(len(haystack)):
#             letter = haystack[right]
#             window_map[letter] = window_map.get(letter, 0) + 1
            
#             if letter not in needle_map:
#                 left = right + 1
#                 window_map = {}
                
#             if right - left + 1  == len(needle):
#                 print(window_map, right, left)
#                 if window_map == needle_map:
#                     return left
                
#                 window_map[haystack[left]] -= 1
#                 if window_map[haystack[left]] == 0:
#                     del window_map[haystack[left]]
                    
#                 left += 1
            
#         return -1 

        return haystack.find(needle)
    
            
            
        
        
        