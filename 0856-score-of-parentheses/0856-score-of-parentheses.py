class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        
        stack = []
        
        for char in s:
            
            if char == '(':
                stack.append(char)
            else:
                # pop opening bracket
                result = 0
                prev = 0
                value = stack.pop()
                if value == '(':
                    result = 1 
                else:
                    if stack and stack[-1] == '(':
                        stack.pop()
                        value *= 2
                    result = value
                #add up the prev value
                if stack and type(stack[-1]) == int:
                    prev = stack.pop()
                stack.append(prev + result)
                
        return stack[-1]
                
                
                
                
                
                
        
        
        
        
        