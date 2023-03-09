class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        
        total_sum = [0]
        curr_sum = 0
        
        def backtrack(total_sum, curr_sum, curr_idx):
            
            if curr_idx >= len(nums):
                total_sum[-1] += curr_sum
                return
            
            
            backtrack(total_sum, curr_sum ^ nums[curr_idx], curr_idx + 1)
            backtrack(total_sum, curr_sum, curr_idx + 1)
            
        backtrack(total_sum, curr_sum, 0)
        
        return total_sum[0]
            
            
            
            
            
        