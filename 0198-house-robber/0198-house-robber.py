class Solution:
    def __init__(self):
        self.memo = {}
        
    def rob(self, nums: List[int]) -> int:
        
        def backtrack(curr_idx):

            if curr_idx not in self.memo:
                self.memo[curr_idx] = nums[curr_idx]
                for idx in range(curr_idx+2, len(nums)):
                    self.memo[curr_idx] = max(self.memo.get(curr_idx, 0), nums[curr_idx] + backtrack(idx))                    
                
            return self.memo[curr_idx]
        
        money = 0
        for idx in range(len(nums)):
            money = max(money, backtrack(idx))
            
        return money
        