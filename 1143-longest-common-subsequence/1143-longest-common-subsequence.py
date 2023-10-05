class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        n, m = len(text1), len(text2)
        dp = {}
        dp[(n, m)] = 0
        
        for ptr1 in range(n-1, -1, -1):
            for ptr2 in range(m-1, -1, -1):
                if text1[ptr1] == text2[ptr2]:
                    dp[(ptr1, ptr2)] = 1 + dp[(ptr1+1, ptr2+1)] if (ptr1+1 < n and ptr2+1 < m) else 1 
                else:
                    dp[(ptr1, ptr2)] = max(dp[(ptr1+1, ptr2)] if ptr1+1 < n else 0, dp[(ptr1, ptr2+1)] if ptr2+1 < m else 0)
                    
        return dp[(0,0)]
                
        
# top-down   
# class Solution:
#     def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
#         memo = {}
#         def dfs(ptr1, ptr2):
            
#             if ptr1 >= len(text1) or ptr2 >= len(text2):
#                 return 0
#             if (ptr1, ptr2) not in memo:
#                 if text1[ptr1] == text2[ptr2]:
#                     memo[(ptr1, ptr2)] = 1 + dfs(ptr1+1, ptr2+1)
#                 else:
#                     memo[(ptr1, ptr2)] = max(dfs(ptr1+1, ptr2), dfs(ptr1, ptr2+1))
                
#             return memo[(ptr1, ptr2)]
            
#         return dfs(0, 0)