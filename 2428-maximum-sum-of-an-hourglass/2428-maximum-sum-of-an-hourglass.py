from typing import List


class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        row_length, col_length  = len(grid), len(grid[0])
        
        max_sum = 0
        
        for i in range(1, row_length-1):
            for j in range(1, col_length-1):
                curr_sum = self.get_hourglass(grid, i, j)
                
                max_sum = max(max_sum, curr_sum)
        
        
        return max_sum
#         return max(
#             self.get_hourglass(grid, i, j)
#             for i in range(1, row_length - 1)
#             for j in range(1, col_length - 1)
#         )


    def get_hourglass(self, grid: List[List[int]], i: int, j: int) -> int:
        return grid[i - 1][j - 1] + grid[i - 1][j] + grid[i - 1][j + 1] + \
                                    grid[i][j] + \
               grid[i + 1][j - 1] + grid[i + 1][j] + grid[i + 1][j + 1]