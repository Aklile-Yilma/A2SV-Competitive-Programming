class Solution:
    def interpret(self, command: str) -> str:
        
        
        idx = 0
        interpretation = ""
        
        while idx < len(command):
            if(command[idx] == "G"):
                interpretation += "G"
                # move index by one 
                idx += 1
                
            elif( command[idx] == "("):
                if(command[idx+1] == ")"):
                    interpretation += "o"
                    # move index by two to skip () brackets 
                    idx += 2
                else:
                    interpretation += "al"
                    # move index by four to skip (al)
                    idx += 4
                    
        return interpretation
                    
                    
                    
            
        
        
        