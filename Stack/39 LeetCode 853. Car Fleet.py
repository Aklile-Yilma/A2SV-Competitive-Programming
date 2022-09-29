from typing import * 
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:


        pair = [[p, s] for p,s in zip(position,speed)]

        stack = []

        
        for p,s in sorted(pair)[::-1]:
            stack.append((target-p)/s)
            if(len(stack)>=2 and stack[-1] <= stack[-2]):
                stack.pop()

        #print(sorted(pair)[::-1])

        return len(stack)



s = Solution()
s.carFleet(12, [10,8,0,5,3], [2,4,1,1,3])