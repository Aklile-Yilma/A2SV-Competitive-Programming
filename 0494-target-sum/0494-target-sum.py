class Solution:
    def __init__(self):
        self.memo = {}
        
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        def backtrack(curr_idx, curr_sum):
            
            if curr_idx == len(nums):
                if curr_sum == target:
                    return 1
                return 0
            
            if (curr_idx, curr_sum) not in self.memo:
                self.memo[(curr_idx, curr_sum)] = backtrack(curr_idx + 1, curr_sum + nums[curr_idx]) + backtrack(curr_idx + 1, curr_sum - nums[curr_idx])
            
            return self.memo[(curr_idx, curr_sum)]
        
        return backtrack(0, 0)
        
        
            
            
        