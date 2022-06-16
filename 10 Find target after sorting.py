# nlogn solution
class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums= sorted(nums)
        
        idx=[]
        for i in range(len(nums)):
            if(target==nums[i]):
                idx.append(i)
                
        return idx
    
#   O(n) solution 
# class Solution:
#     def targetIndices(self, nums, target):
#         idx = cnt = 0
#         for num in nums:
#             idx += num < target
#             cnt += num == target
#         return list(range(idx, idx+cnt))
        