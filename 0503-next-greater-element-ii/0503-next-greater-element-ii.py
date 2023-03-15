class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        ans = [-1] * len(nums)
        stack = []
        
        for idx, num in enumerate(nums):
            
            while stack and nums[stack[-1]] < num:
                ans[stack.pop()] = num
                
            stack.append(idx)
            
            
        for num in nums:
            while stack and nums[stack[-1]] < num:
                ans[stack.pop()] = num
            
        return ans
        