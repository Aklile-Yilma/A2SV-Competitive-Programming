class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        
        for ptr in range(len(nums)):
            
            while nums[ptr] != ptr + 1 and nums[ptr] > 0 and nums[ptr] < len(nums):
                corr_pos = nums[ptr] - 1
                if nums[ptr] == nums[corr_pos]:
                    break
                nums[ptr], nums[corr_pos] = nums[corr_pos], nums[ptr]
                
                
        for idx in range(len(nums)):
            
            if nums[idx] != idx + 1:
                return idx + 1
            
        return len(nums) + 1