class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        
        """
        Create a monotonically increasing stack if the item to be inserted is smaller the elements in the stack 
        then remove those elements using while loop
        """
        mono_stack = []
        
        for i in num:
            while k>0 and mono_stack and (int(mono_stack[-1]) > int(i)):
                mono_stack.pop()
                k-=1
            mono_stack.append(i)


        #if loop has ended and k>0
        mono_stack = mono_stack[:len(mono_stack) - k]
        result = "".join(mono_stack)
    
        #last check if result is an empty string  to return 0
        #remove leading zeros
        return str(int(result)) if result else 0
            
        
                    
                
s= Solution()
print(s.removeKdigits("1432219", 3))
