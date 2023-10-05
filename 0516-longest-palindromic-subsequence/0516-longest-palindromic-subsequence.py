class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        
        # same concept as 1143
        n = len(s)
        dp = {}
        dp[(n, -1)] = 0
        
        for right in range(n-1, -1, -1):
            for left in range(n):

                if s[right] == s[left]:
                    dp[(right, left)] = 1 + dp[(right+1, left-1)] if (right+1 < n and left-1 >= 0) else 1
                else:
                    ans1 = dp[(right+1, left)] if right+1 < n else 0
                    ans2 = dp[(right, left-1)] if left-1 >= 0 else 0
                    dp[(right, left)] = max(ans1, ans2)
                    
        return dp[(0, n-1)]

    
# top-down
# class Solution:
#     def longestPalindromeSubseq(self, s: str) -> int:
        
        
#         n = len(s)
#         memo = {}
#         # same concept as 1143
        
#         def dfs(to_right, to_left):
            
#             if to_right >= n or to_left < 0:
#                 return 0
            
#             if (to_right, to_left) not in memo:
#                 if s[to_right] == s[to_left]:
#                     memo[(to_right, to_left)] = 1 + dfs(to_right + 1, to_left - 1)
#                 else:
#                     memo[(to_right, to_left)] = max(dfs(to_right+1, to_left), dfs(to_right, to_left-1))
                
#             return memo[(to_right, to_left)]
            
            
#         return dfs(0, n-1)