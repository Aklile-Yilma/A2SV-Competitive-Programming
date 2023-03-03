# class Solution:
#     def decodeString(self, s: str) -> str:
#         stack = []
        
#         for i in range(len(s)):
#             if s[i] != "]":
#                 #appending characters 
#                 stack.append(s[i])
#             else:
                
#                 substr = ""
                
#                 while stack[-1] != "[":
#                     #create substring keeping the order
#                     substr = stack.pop() + substr
                    
#                 # remove the opening bracket from the stack    
#                 stack.pop()
                
#                 k = ""
#                 while stack and stack[-1].isdigit():
#                     #create num keeping the order
#                     k = stack.pop() + k
                
#                 # append substring k times
#                 stack.append(int(k) * substr)
                
#         return ''.join(stack)
    
    
class Solution:
    def decodeString(self, s: str) -> str:
        idx = 0                                      # index pointer for 's' string
        def decode(s, mult=1) -> str:                # define recursive decode helper function
            nonlocal idx                             # reference our index pointer
            
            curr_str = ''                            # begin with an empty string
            while idx < len(s):                      # while there remains un-parsed letters
                if s[idx].isdigit():                 # parse digit, triggers recursive call
                    curr_mult = ''                   # derive the multiplier
                    while idx < len(s) and s[idx].isdigit():          # parse all digits
                        curr_mult += s[idx]
                        idx += 1
                    idx += 1                         # move the pointer past left bracket '['
                    curr_str += decode(s, mult=int(curr_mult))  # recursive call
                elif s[idx].isalpha():               # parse alphabet char, build the string
                    curr_str += s[idx]
                    idx += 1
                else:                                # parse right bracket ']', call end condition
                    idx += 1
                    return mult * curr_str           # multiply the resulting string from this call and return
            return mult * curr_str
        return decode(s)


               
        
        


        
        
        
        
        

                
        
        
        