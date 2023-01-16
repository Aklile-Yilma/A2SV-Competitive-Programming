class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        row_length = len(grid)
        
        ans = [[0]*(row_length-2) for _ in range(row_length-2)]
        
        for i in range(row_length-2): 
            for j in range(row_length-2): 
                ans[i][j] = max(grid[ii][jj] for ii in range(i, i+3) for jj in range(j, j+3))
                
        return ans 