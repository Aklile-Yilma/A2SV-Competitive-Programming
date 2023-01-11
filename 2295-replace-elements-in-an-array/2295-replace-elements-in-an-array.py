class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        
        nums_map = {}
        # nums = [None] * len(nums)
        for idx, num in enumerate(nums):
            nums_map[num] = idx
                    
        for num, replacement in operations:
            idx = nums_map[num]
            del nums_map[num]
            nums[idx] = replacement
            nums_map[replacement] = idx
            
        return nums
            
            
            
        