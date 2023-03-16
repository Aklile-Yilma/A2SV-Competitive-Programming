class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        curr_sub = []
        subsets = [[]]
        
        def backtrack(start, curr_sub):
            
            if start >= len(nums):
                return
            
            
            for j in range(start, len(nums)):
                curr_sub.append(nums[j])
                subsets.append(curr_sub.copy())
                backtrack(j+1, curr_sub)
                curr_sub.pop()
                
            return
        
        backtrack(0, curr_sub)
        return subsets