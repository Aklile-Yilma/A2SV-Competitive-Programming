class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        # to get range of number from 0  to n
        n = len(nums) + 1
        nums = set(nums)
        
        
        for num in range(n):
            # o(1) to check an item is in a set
            if(num not in nums):
                return num
            
        return -1