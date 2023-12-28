class Solution:
    def maxNonDecreasingLength(self, nums1: List[int], nums2: List[int]) -> int:
        
        max_len = 1
        n = len(nums1)
        
        @cache
        def dfs(idx, prev):
            nonlocal max_len
            if idx >= n:
                return 0
            
            res = 0
            if not prev:
                res = dfs(idx+1, prev)
                
            if prev <= nums1[idx]:
                res = max(res, 1 + dfs(idx+1, nums1[idx]))
            if prev <= nums2[idx]:
                res = max(res, 1 + dfs(idx+1, nums2[idx]))
                
            return res
        
        return dfs(0, 0)
        
            