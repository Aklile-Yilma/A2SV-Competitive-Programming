class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:

                    
        dp = {}
        
        for right in range(len(nums)):
            # check with previous
            for left in range(right):
                diff = nums[right] - nums[left]
                # find sequence with current difference and add 1
                dp[(right, diff)] = 1 + dp.get((left, diff), 1)
                
        return max(dp.values())