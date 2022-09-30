from typing import *

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        prefix = [0]
        left = 0
        right = left + 1
        count = 0

        for i in nums:
            prefix.append(prefix[-1] + i)
            
        # print(prefix_sum)
        print(prefix)
            
            
#         for i in nums:
#             if(i == k):
#                 count+=1

        while left < right and left + 1 < len(prefix):
 

           
            if(prefix[right] - prefix[left] == k):
                count+=1   
                
            right+=1
            if( (right) >= len(prefix)):
                left+=1
                right = left + 1                 
           
            
            
            #     # # left+=1
            # else:
            #     # to escape the while loop from stopping if right reaches len(prefix) before left is at the right most index        
            #     # if( (right + 1) == len(prefix)):
            #     #     left+=1
            #     #     right = left + 1
                    
            #     right +=1
            #     # else:
            #     #     right+=1
                    
            
        return count
    
s = Solution()
print(s.subarraySum([1,-1,0],0))