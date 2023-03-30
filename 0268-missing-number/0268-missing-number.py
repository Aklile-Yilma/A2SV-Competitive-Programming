
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        xor_nums = 0
        for num in nums:
            xor_nums ^= num
            
        xor_all = 0
        for idx in range(len(nums)+1):
            xor_all ^= idx
            
        return xor_nums ^ xor_all


#using cyclic sort
# class Solution:
#     def missingNumber(self, nums: List[int]) -> int:
        
#         idx = 0
    
#         while idx < len(arr):
#             if arr[idx] != idx and arr[idx] < len(nums):
#                 corr_pos = arr[idx] 
#                 arr[idx], arr[corr_pos] = arr[corr_pos], arr[idx]
#             else:
#                 idx += 1 
                
#         for idx in range(len(nums)):
#             if idx != nums[idx]:
#                 return idx
        
#         return len(nums)
    
    

        
        