class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        m = len(nums2)
        dp = {}
        
        def dfs(i, j):
            if i >= n or j >= m:
                return 0
            
            if (i, j) in dp:
                return dp[(i, j)]
            
            if nums1[i] == nums2[j]:
                dp[(i, j)] = 1 + dfs(i+1, j+1)
            else:
                 dp[(i, j)] = max(dfs(i, j+1), dfs(i+1, j))
            
            return dp[(i, j)]
        
        return dfs(0, 0)