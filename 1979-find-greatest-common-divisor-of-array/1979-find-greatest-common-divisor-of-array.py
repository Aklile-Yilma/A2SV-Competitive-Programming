class Solution:
    def findGCD(self, nums: List[int]) -> int:
        
        small = min(nums)
        large = max(nums)
        
        def GCD(large, small):
            if small == 0:
                return large
            
            return GCD(small, large % small)
        
        
        return GCD(large, small)