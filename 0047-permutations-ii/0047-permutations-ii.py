class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        result_set = set()
        
        def backtrack(curr, curr_set):
            
            nonlocal result
            
            if len(curr) == len(nums):
                if tuple(curr) not in result_set:
                    result.append(curr.copy())
                    result_set.add(tuple(curr))
                return
            
            for idx in range(len(nums)):
                
                if idx not in curr_set:
                    curr.append(nums[idx])
                    curr_set.add(idx)
                    
                    backtrack(curr, curr_set)
                    
                    curr.pop()
                    curr_set.remove(idx)
                
            return
        
        backtrack([], set())
        
        return result
            
            