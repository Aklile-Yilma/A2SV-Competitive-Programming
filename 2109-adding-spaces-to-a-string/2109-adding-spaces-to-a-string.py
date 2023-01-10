class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        
        s_list = []
    
        spaces = set(spaces)
    
        for idx, letter in enumerate(s):
            
            if(idx in spaces):
                s_list.append(" ")
                
            s_list.append(letter)
            
        return "".join(s_list)
        
            
        
            
            
            
        
