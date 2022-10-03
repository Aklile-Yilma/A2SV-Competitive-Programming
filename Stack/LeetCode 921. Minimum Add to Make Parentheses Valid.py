 class Solution:
    def minAddToMakeValid(self, s: str) -> int:

        stack = 0
        var = 0
        for i in s:
            if i == "(":
                stack +=1
            else:
                if not stack:
                    var +=1
                else:
                    stack-=1

        return stack + var
