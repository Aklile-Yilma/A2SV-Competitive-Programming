class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        n = len(nums) + 1
        
        nums = set(nums)
        
        for num in range(n):
            if(num not in nums):
                return num
            
        return -1