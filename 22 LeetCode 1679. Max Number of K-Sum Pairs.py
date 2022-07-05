class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        
        sums = 0        # set counter sums at 0, then sort nums
        sorts = sorted(nums)
        
        l = 0       # using two pointer approach, set l = 0, r = len(nums) - 1
        r = len(nums) - 1
        
        while l < r:        # while l < r, if sorts[l] + sorts[r] > k, reduce r by 1, if sorts[l] + sorts[r] < k, increase l by 1. if sorts[l] + sorts[r] = k, increase l by 1 and decrease r by 1. 
            if sorts[l] + sorts[r] > k:
                r -= 1
            elif sorts[l] + sorts[r] < k:
                l += 1
            else:
                sums += 1
                l += 1
                r -= 1
        
        return sums 
