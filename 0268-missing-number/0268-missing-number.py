class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        # to get range of number from 0  to n
        
        
        for ptr in range(len(nums)):
            
            while nums[ptr] != ptr and nums[ptr] < len(nums):
                
                right = nums[ptr]
                
                nums[ptr], nums[right] = nums[right], nums[ptr]
                
            
        for idx in range(len(nums)):
            if nums[idx] != idx:
                return idx
            
        return len(nums)
                