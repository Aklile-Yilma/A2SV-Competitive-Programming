class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        result = []
        # keep track if we are in /* */ comment
        is_comment = ""
        # current none comment string
        substring = ""        
        
        for line in source:
            idx = 0
            while idx < len(line):
                if not is_comment and line[idx:idx+2] == '//':
                    break

                elif line[idx:idx+2] == '/*':
                    if not is_comment:
                        is_comment = True
                        idx += 1

                elif is_comment and line[idx:idx+2] == '*/':
                    is_comment = False
                    idx += 1
                
                elif not is_comment:
                    #add each character to substring
                    substring += line[idx]                
                    
                idx += 1
                
            if substring and not is_comment:
                result.append(substring)
                substring = ""

        return result
                
                    
                
                    
                    
                
                    
                    
                    
                
                    
                
                    
            
            
            
        
        
        