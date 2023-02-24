class Solution:
    def simplifyPath(self, path: str) -> str:
        
        paths = path.split('/')
        stack = []
                
        for path in paths:
            
            if path == "..":
                if stack:
                    stack.pop()
            elif not (path == '.' or path == ''):
                stack.append(path)
           
        simplified = '/'.join(stack)
        
        return "/" + simplified
            
        
            
