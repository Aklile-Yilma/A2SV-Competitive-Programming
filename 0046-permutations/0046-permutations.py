class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        permutations = []
        curr_perm = []
        
        def backtrack(curr_perm, num):
            if len(curr_perm) == len(nums):
                permutations.append(curr_perm.copy())
                return
            
            for idx in range(len(nums)):
                is_visited = num & (1 << idx)
                if not is_visited:
                    #place candidate
                    curr_perm.append(nums[idx])
                    
                    #backtrack
                    backtrack(curr_perm,  num | (1 << idx))
                    
                    #remove candidate
                    item = curr_perm.pop()
                    # num = num ^ (1 << idx)
                    
            return
        
        
        backtrack(curr_perm, 0)
        
        return permutations
        
        