class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        permutations = []
        curr_perm = []
        
        
        def backtrack(curr_idx, curr_perm):
            
            if len(curr_perm) == len(nums):
                permutations.append(curr_perm.copy())
                return
            
            for idx in range(len(nums)):
                
                if nums[idx] not in curr_perm:
                    curr_perm.append(nums[idx])
                    backtrack(idx, curr_perm)
                    curr_perm.pop()
                    
            return
        
        
        backtrack(-1, curr_perm)
        
        return permutations
        
        