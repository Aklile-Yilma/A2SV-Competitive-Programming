class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:


        A = arr
        res = []
        for x in range(len(A), 1, -1):
            i = A.index(x)
            res.extend([i + 1, x])
            A = A[:i:-1] + A[:i]
        return res

