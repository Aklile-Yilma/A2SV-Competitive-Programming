class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        
        ans = [None] * len(nums)
        
        for idx, num in enumerate(nums):
            ans[idx] = nums[num]
            
        return ans
        