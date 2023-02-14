class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        map_ts = {}
        map_st = {}
        
        for char_s, char_t in zip(s, t):
            if (char_s in map_st and char_t != map_st[char_s]) or (char_t in map_ts and char_s != map_ts[char_t]):
                    return False
                
            map_st[char_s] = char_t
            map_ts[char_t] = char_s
                
        return True
            
        