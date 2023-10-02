class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:

                    
        dp = {}
        
        for right in range(len(nums)):
            for left in range(right):
                diff = nums[right] - nums[left]
                dp[(right, diff)] = 1 + dp.get((left, diff), 1)
                
        return max(dp.values())