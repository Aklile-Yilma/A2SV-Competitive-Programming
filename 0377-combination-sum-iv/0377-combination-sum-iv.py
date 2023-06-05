class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:

        dp = [0] * (target + 1)
        dp[0] = 1
        
        for amt in range(1, target+1):
            for num in nums:
                dp[amt] += dp[amt - num] if amt - num >= 0 else 0
              
        return dp[target]
        