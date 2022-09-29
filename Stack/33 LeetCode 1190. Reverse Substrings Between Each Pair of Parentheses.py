class Solution:
    def reverseParentheses(self, s: str) -> str:
        
        stack = list(s)
        left_pointers = []
        
        for idx,value in enumerate(stack):
            if ( value == '('):
                left_pointers.append(idx)
            elif ( value == ')'):
                right = idx
                left = left_pointers.pop()
                stack[left:right] = stack[left:right][::-1]
                stack.pop(idx)
                stack.insert(idx, "")
                stack.pop(idx-1)
                stack.insert(idx-1, "")
            else:
                continue

                
        return ''.join(stack)
        
s= Solution()
print(s.reverseParentheses("(ed(et(oc))el)"))
         
