class Solution:
    def maxDepth(self, s: str) -> int:

        stack = 0
        result = 0

        for item in s:
            if(item == "("):
                stack += 1
            elif(item == ")"):
                stack -= 1


            # keep track of the largest nesting
            result = max(result , stack)


        return result
