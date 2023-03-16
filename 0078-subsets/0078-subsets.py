class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        curr_sub = []
        curr_subset = set()
        subsets = []
        
        def backtrack(start, curr_sub):
            
            if tuple(curr_sub) not in curr_subset:
                curr_subset.add(tuple(curr_sub))
                subsets.append(curr_sub.copy())
            
            if start >= len(nums):
                return
            
            
            for j in range(start, len(nums)):
                curr_sub.append(nums[j])
                backtrack(j+1, curr_sub)
                curr_sub.pop()
                
            return
        
        backtrack(0, curr_sub)
        return subsets