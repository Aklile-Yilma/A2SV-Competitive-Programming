class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
                
 
        row_length = len(grid)
        col_length = len(grid[0])
        
        # represents summation of all 1 in a row
        ones_row = [0] * row_length
        # represents summation of all 1 in a col
        ones_col = [0] * col_length
        
        for i in range(row_length):
            for j in range(col_length):
                if grid[i][j] == 1:
                    ones_row[i] += 1
                    ones_col[j] += 1
        
        
        diff = [[0] * col_length for _ in range(row_length)]


    
        for i in range(row_length):
            for j in range(col_length):
                # we can find the number of zeros by subtracting from row/col length
                diff[i][j] = ones_row[i] + ones_col[j] - (row_length - ones_row[i]) - (col_length - ones_col[j])
        
        return diff
    