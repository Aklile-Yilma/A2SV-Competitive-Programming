from typing import *
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        # is added to the stack
        isAdded = True
        stack = []

        #iterate over num1
        for i in nums1:
            # find i index in num2
            idx = nums2.index(i)

            # iterate from idx
            for i in range(idx, len(nums2),1):

                # if numbers after that idx is greater then append greater element idx
                if(nums2[idx] < nums2[i]):
                    stack.append(nums2[i])
                    isAdded = True
                    break#

                # if i is the last element set isAdded to false
                if(i == len(nums2)-1):
                    isAdded = False

            # if greater element is not found append -1
            if not isAdded:
                stack.append(-1)

        return stack

s = Solution()
print(s.nextGreaterElement([4,1,2],[1,3,4,2]))
