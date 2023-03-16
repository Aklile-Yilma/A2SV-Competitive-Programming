class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        ans = []
        curr_cand = []
        curr_subset = set()
        def backtrack(start, curr_cand, total):

            
            if start >= len(candidates) or total > target:
                return
            
            for idx in range(start, len(candidates)):
                curr_cand.append(candidates[idx])
                #check
                total = sum(curr_cand)
                if total == target:
                    ans.append(curr_cand.copy())
                    
                backtrack(idx , curr_cand, total)
                curr_cand.pop()
                
            return 
        
        backtrack(0, curr_cand, 0)
        
        return ans
        