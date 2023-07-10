class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        ans = nums[0]
        total = nums[0]
        
        for idx in range(1, len(nums)):
            total += nums[idx]
            ans = max(ans, math.ceil(total / (idx + 1)))
            
        return ans