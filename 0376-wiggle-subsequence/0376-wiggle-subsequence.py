class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        
        size = len(nums)
        dp = [[1, 1] for _ in range(size)]
        
        
        for right in range(size):
            for left in range(right):
                val = nums[right] - nums[left]
                if val > 0:
                    dp[right] = [dp[right][0], max(dp[right][1], dp[left][0] + 1)]
                elif val < 0:
                    dp[right] = [max(dp[right][0], dp[left][1] + 1), dp[left][1]]
                    
                    
        max_size = 0
        for pos_seq, neg_seq in dp:
            max_size = max(max_size, pos_seq)
            max_size = max(max_size, neg_seq)            
            
            
        return max_size