class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        curr_comb = []
        comb = []
        
        def backtrack(comb, curr_comb, n, k):
            
            if len(curr_comb) == k:
                comb.append(curr_comb.copy())
                return
            
            start = 1 if not curr_comb else curr_comb[-1] + 1
            
            for j in range(start, n+1):
                curr_comb.append(j)
                backtrack(comb, curr_comb, n, k)
                curr_comb.pop()
                
            return 
        
        backtrack(comb, curr_comb, n, k)
        return comb
        
                
            
        