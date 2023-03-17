class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        #sort
        candidates.sort()
        
        ans = []
        curr_cand = []
        
        def backtrack(start, curr_cand, total):

            
            if start >= len(candidates) or total > target:
                return
            
            for idx in range(start, len(candidates)):
                
                #prune
                if idx > start and candidates[idx] == candidates[idx - 1]:
                    continue
                else:
                    curr_cand.append(candidates[idx])
                    #check
                    total = sum(curr_cand)
                    if total == target:
                        ans.append(curr_cand.copy())

                    backtrack(idx + 1 , curr_cand, total)
                    curr_cand.pop()
                    
            return 
        
        backtrack(0, curr_cand, 0)
        
        return ans