from typing import *
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack  = []
        
        
        for i in tokens:
            #why is lstrip working?
            if(i.lstrip('-+').isdigit()):
                stack.append(int(i))
            else: 
                #order of popping is important the earlier number in the list "operation" the latter number
                num1=stack.pop()
                num2=stack.pop()
                print('')
                if i == '+': stack.append(num2 + num1)
                elif i == '-': stack.append(num2 - num1)
                elif i == '*': stack.append(num2 * num1)
                else : stack.append(int(num2/num1))
                      
        return stack[-1]
        
         
s = Solution()
print(s.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))