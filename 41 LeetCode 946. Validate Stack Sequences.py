from typing import *

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        
        
        start_idx = 0
        stack = []
        
        for i in popped:
            idx = pushed.index(i);
            if i not in stack:
                stack.extend(pushed[start_idx : idx+1])
                start_idx = idx+1
                stack.pop()
            elif stack[-1] == i:
                stack.pop()
            else:
                return False
            
        return True
                

s = Solution()
s.validateStackSequences([1,2,3,4,5], [4,5,3,2,1])