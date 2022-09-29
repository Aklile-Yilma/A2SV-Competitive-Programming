from typing import *
class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        
        queue = []
        total = 0
        
        for i in nums:
            #total = sum(queue)
            if(k == i):
                return 1
            elif(total != k  and i<=k):
                total+=i
                queue.append(i)
                continue
            break
        
        return len(queue) if total==k else -1

s= Solution()
print(s.shortestSubarray([77,19,35,10,-14], 19))

