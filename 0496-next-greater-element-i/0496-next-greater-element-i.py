class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        next_greater = {}
        ans = []
        stack = []
        
        for num in nums2:

            while stack and stack[-1] <= num:
                next_greater[stack.pop()] = num

            stack.append(num)

        for num in nums1:
            ans.append(next_greater.get(num, -1))

        return ans

            
    
    