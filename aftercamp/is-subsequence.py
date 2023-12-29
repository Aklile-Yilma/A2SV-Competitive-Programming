class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        if len(t) == 0 and len(s) != 0:
            return False

        i, j = 0, 0
        ans = True

        for j in range(len(t)):
            if i < len(s) and s[i] == t[j]:
                i += 1

        return True if i == len(s) else False

# class Solution:
#     def isSubsequence(self, s: str, t: str) -> bool:
        
#         n = len(s)
#         memo = {}
#         def dfs(i, j):
            
#             print(i, j)
#             if i >= n:
#                 return True
            
#             if j >= len(t):
#                 return False
            
#             if (i, j) not in memo:
#                 if s[i] == t[j]:
#                     memo[(i, j)] = dfs(i+1, j+1)
#                 else:
#                     memo[(i, j)] = dfs(i, j+1)

#             return memo[(i, j)]
            
#         return dfs(0, 0)