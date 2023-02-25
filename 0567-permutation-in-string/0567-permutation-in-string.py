class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        left = 0
        s1_counter = Counter(s1)
        window_map = {}
        
        for right in range(len(s2)):
            char = s2[right]
            
            if char in s1_counter: 
                if char not in window_map.keys():
                    window_map[char] = 1
                else:
                    window_map[char] += 1
            else:
                left = right + 1
                window_map = {}
                
            #check window
            if right - left + 1 == len(s1):
                if s1_counter == window_map:
                    return True
                window_map[s2[left]]-= 1
                if window_map[s2[left]] == 0:
                    del window_map[s2[left]]
                left += 1
                
        return False