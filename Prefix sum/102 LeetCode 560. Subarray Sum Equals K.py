from typing import *

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        prefix = [0]
        left = 0
        right = left + 1
        count = 0

        for i in nums:
            prefix.append(prefix[-1] + i)
            
        print(prefix)
            
        # works but results time limit exceeded because it iterates back and forth for each left item
        while left < right and left + 1 < len(prefix):
 
            if(prefix[right] - prefix[left] == k):
                count+=1   
                
            right+=1
            if( (right) >= len(prefix)):
                left+=1
                right = left + 1                 

            
        return count
    
s = Solution()
print(s.subarraySum([1,-1,0],0))