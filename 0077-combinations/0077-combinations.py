class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        curr_comb = []
        comb = []
        
        def backtrack(start, curr_comb):
            
            if len(curr_comb) == k:
                comb.append(curr_comb.copy())
                return
            
            
            for j in range(start, n+1):
                curr_comb.append(j)
                backtrack(j + 1, curr_comb)
                curr_comb.pop()
                
            return 
        
        backtrack(1, curr_comb)
        return comb
        
                
            
        