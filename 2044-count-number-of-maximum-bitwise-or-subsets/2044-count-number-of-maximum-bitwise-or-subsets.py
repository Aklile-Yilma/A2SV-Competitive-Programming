class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_or = 0
        for num in nums:
            max_or = max(max_or, max_or | num)
            
        count = 0
        
        def backtrack(start, curr_or):
            nonlocal max_or, count
            
            if curr_or ==  max_or:
                count += 1
                
            if start >= len(nums):
                return
            
            for idx in range(start, len(nums)):
                backtrack(idx + 1, curr_or | nums[idx])
                                
            return 
        
        backtrack(0, 0)
        
        return count
        
        
        