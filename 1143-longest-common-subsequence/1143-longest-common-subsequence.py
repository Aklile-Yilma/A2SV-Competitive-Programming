class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        memo = {}
        def dfs(ptr1, ptr2):
            
            if ptr1 >= len(text1) or ptr2 >= len(text2):
                return 0
            if (ptr1, ptr2) not in memo:
                if text1[ptr1] == text2[ptr2]:
                    memo[(ptr1, ptr2)] = 1 + dfs(ptr1+1, ptr2+1)
                else:
                    memo[(ptr1, ptr2)] = max(dfs(ptr1+1, ptr2), dfs(ptr1, ptr2+1))
                
            return memo[(ptr1, ptr2)]
            
        return dfs(0, 0)