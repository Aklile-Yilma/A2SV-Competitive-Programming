class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        nums.insert(0, -inf)
        lengths = [1] * len(nums)
        lengths[0] = 0
        for i in range(1, len(nums)):
            _max = -inf
            for j in range(i):
                if nums[j] < nums[i]:
                    _max = max(_max, lengths[j] + 1)
            lengths[i] = max(lengths[i], _max)

        return max(lengths)


# class Solution:
#     def lengthOfLIS(self, nums: List[int]) -> int:
        
#         @cache
#         def dfs(prev, idx):
            
#             if idx == len(nums):
#                 return 0
            
#             pick = 0
#             if nums[idx] > nums[prev]:
#                 pick = 1 + dfs(idx, idx+1)
#             np = dfs(prev, idx+1)
            
#             return max(pick, np)
        
#         nums.insert(0, -100000)
#         return dfs(0, 1)
            