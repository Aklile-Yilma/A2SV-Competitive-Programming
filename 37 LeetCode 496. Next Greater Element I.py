from typing import *
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        isAdded = True
        stack = []
        for i in nums1:
            idx = nums2.index(i)
            for i in range(idx, len(nums2),1):
                if(nums2[idx] < nums2[i]):
                    stack.append(nums2[i])
                    isAdded = True
                    break
                if(i == len(nums2)-1):
                    isAdded = False
            if not isAdded:    
                stack.append(-1)
                   
        return stack

s = Solution()
print(s.nextGreaterElement([4,1,2],[1,3,4,2]))