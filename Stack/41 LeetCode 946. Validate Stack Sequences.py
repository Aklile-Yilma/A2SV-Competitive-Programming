from typing import *

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:


        start_idx = 0
        stack = []

        # iterated though popped items
        for popped_item in popped:
            # get the index of the first popped item IN pushed list
            idx = pushed.index(popped_item)

            if popped_item not in stack:
                # create/(extend if not empty) a stack from the pushed list upto the first popped item
                stack.extend(pushed[start_idx : idx+1])
                # set start index to the next popped element index
                start_idx = idx+1
                stack.pop()

            elif stack[-1] == popped_item:
                stack.pop()

            else:
                return False

        return True

s = Solution()
s.validateStackSequences([1,2,3,4,5], [4,5,3,2,1])
