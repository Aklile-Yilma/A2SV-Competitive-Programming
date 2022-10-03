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
                # reversing the letters within the brackets
                stack[left:right] = stack[left:right][::-1]
                #removing the closing bracket
                stack.pop(idx)
                # making sure our list/stack doesn't decrease in size
                stack.insert(idx, "")
                # removing the opening bracket
                stack.pop(idx-1)
                stack.insert(idx-1, "")
            else:
                continue


        return ''.join(stack)

        
s= Solution()
print(s.reverseParentheses("(ed(et(oc))el)"))
         
