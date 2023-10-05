class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        
        n = len(s)
        memo = {}
        # same concept as 1143
        
        def dfs(to_right, to_left):
            
            if to_right >= n or to_left < 0:
                return 0
            
            if (to_right, to_left) not in memo:
                if s[to_right] == s[to_left]:
                    memo[(to_right, to_left)] = 1 + dfs(to_right + 1, to_left - 1)
                else:
                    memo[(to_right, to_left)] = max(dfs(to_right+1, to_left), dfs(to_right, to_left-1))
                
            return memo[(to_right, to_left)]
            
            
        return dfs(0, n-1)