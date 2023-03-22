class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        
        sub = []
        sub_set = set()
        
        def backtrack(start, curr_sub):
        
            if start >= len(nums):
                return
            
            for idx in range(start, len(nums)):
                curr_sub.append(nums[idx])
                
                if len(curr_sub) > 1 and curr_sub[-1] >= curr_sub[-2] or len(curr_sub) <= 1:
                    if len(curr_sub) > 1 and tuple(curr_sub) not in sub_set:
                        sub_set.add(tuple(curr_sub.copy()))
                        sub.append(curr_sub.copy())
                    backtrack(idx + 1, curr_sub)
                                
                curr_sub.pop()
                
            return 
        
        backtrack(0, [])
        
        return sub        