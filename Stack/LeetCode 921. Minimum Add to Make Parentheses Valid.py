 class Solution:
    def minAddToMakeValid(self, s: str) -> int:


        stack = 0
        var = 0
        for i in s:
            #if i is opening bracket then increase our stack
            if i == "(":
                stack +=1
            else:
                # if stack is empty by now it must be that we have a closing bracket
                if not stack:
                    var +=1
                else:
                    stack-=1

        return stack + var
