class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]
        
        def helper(arr):
            
            dp = [0, 0]
            
            for num in arr:
                no_steal_prev = dp[1]
                
                dp = [num + no_steal_prev, max(dp)]
                
            return max(dp)
        
        #with pick first
        ans1 = helper(nums[:-1])
        
        #with not pick first
        ans2 = helper(nums[1:])
        
        return max(ans1, ans2)
                
        
        
# top-down
        
# class Solution:
#     def __init__(self):
#         self.memo = {}
        
#     def rob(self, nums: List[int]) -> int:
        
#         if len(nums) == 1:
#             return nums[0]
        
#         def dfs(curr_idx, canPickLast):
#             if curr_idx == len(nums)-1 and not canPickLast:
#                 return 0
            
#             if curr_idx >= len(nums):
#                 return 0
            
#             if (curr_idx, canPickLast) not in self.memo:
#                 #pick 
#                 pick = dfs(curr_idx + 2, canPickLast) + nums[curr_idx]
#                 #not_pick
#                 n_pick = dfs(curr_idx+1, canPickLast)
#                 #find max
#                 self.memo[(curr_idx, canPickLast)] = max(pick, n_pick)
                
#             return self.memo[(curr_idx, canPickLast)]
        
#         return max(dfs(2, False) + nums[0], dfs(1, True))