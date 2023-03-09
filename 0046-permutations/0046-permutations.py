class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        permutations = []
        curr_perm = []
        curr_permset = set()
        
        def backtrack(curr_idx, curr_perm, curr_permset):
            
            if len(curr_perm) == len(nums):
                permutations.append(curr_perm.copy())
                return
            
            for idx in range(len(nums)):
                
                if nums[idx] not in curr_permset:
                    #place candidate
                    curr_perm.append(nums[idx])
                    curr_permset.add(nums[idx])
                    
                    #backtrack
                    backtrack(idx, curr_perm, curr_permset)
                    
                    #remove candidate
                    item = curr_perm.pop()
                    curr_permset.remove(item)
                    
            return
        
        
        backtrack(-1, curr_perm, curr_permset)
        
        return permutations
        
        