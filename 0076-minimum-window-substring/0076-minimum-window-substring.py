class Solution:
    def minWindow(self, s: str, t: str) -> str:

        result = [-1, -1]
        res_len = float('inf')
        t_map = Counter(t)
        window_map = {}
        left = 0
        have = 0
        need = len(t_map)
        
        
        for right in range(len(s)):
            letter = s[right]
            #add to window
            window_map[letter] = window_map.get(letter, 0) + 1
            
            if letter in t_map and window_map[letter] == t_map[letter]:
                have += 1
            
            while have == need:
                if right - left < res_len:
                    result = [left, right]
                    res_len = right - left + 1
                #handle dict
                window_map[s[left]] -= 1
                #handle have
                if s[left] in t_map and window_map[s[left]] < t_map[s[left]]:
                    have -= 1
    
                if window_map[s[left]] == 0:
                    del window_map[s[left]]
                left += 1

        left , right = result[0], result[1] 
        return s[left:right+1] if res_len != float('inf') else ''
        
        

# class Solution:
#     def minWindow(self, s: str, t: str) -> str:
        
#         def check(window_map, t_map):
            
#             for item in t_map:
#                 value = window_map.get(item, 0)
#                 if value == 0 or value < t_map[item]:
#                     return False
                
#             return True
                    
#         result = [float('inf'), float('inf')]
#         t_map = Counter(t)
#         window_map = {}
        
#         left = 0
#         for right in range(len(s)):
#             letter = s[right]
            
#             if letter in window_map:
#                 window_map[letter] += 1
#             else:
#                 window_map[letter] = 1
                
#             while check(window_map, t_map):
#                 if result[1] - result[0] > right - left or result[1] == float('inf') or result[0] == float('inf'):
#                     result = [left, right]
#                 #handle dict
#                 window_map[s[left]] -= 1
#                 if window_map[s[left]] == 0:
#                     del window_map[s[left]]
#                 left += 1
                
#         left , right = result[0], result[1] 
#         return s[left:right+1] if left != float('inf') and right != float('inf') else ''
            
                    
            
        
            
            
            
        
        
        