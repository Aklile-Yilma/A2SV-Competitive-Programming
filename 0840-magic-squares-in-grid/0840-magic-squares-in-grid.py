class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        
        count = 0
        rows, cols = len(grid), len(grid[0])
        
        #grab possible 3x3 matrix
        for r in range(rows - 2):
            for c in range(cols - 2):
                subMatrix = [grid[row_idx][c: c + 3] for row_idx in range(r, r + 3)]
                if self.isMagicSquare(subMatrix):
                    count += 1
    
        return count
        
    def isMagicSquare(self, subMatrix: List[List[int]]) -> int:
        #check duplicates
        digits = {1, 2, 3, 4, 5, 6, 7, 8, 9}
        if set(sum(subMatrix, [])) != digits:
            return False
        
        isMagic = True
        
        row_length = col_length = 3
        #iterate and check rows
        summation = []
        for row_idx in range(row_length):
            summation.append(sum([subMatrix[row_idx][0], subMatrix[row_idx][1], subMatrix[row_idx][2]]))
        
        if len(set(summation)) != 1:
            return False
        
        #iterate and check cols
        summation = []
        for col_idx in range(col_length):
            summation.append(sum([subMatrix[0][col_idx], subMatrix[1][col_idx], subMatrix[2][col_idx]]))
        
        if len(set(summation)) != 1:
            return False
        
        #check the main diagonal
        summation = []
        curr_sum = 0
        for row_idx in range(row_length):
            for col_idx in range(col_length):
                if row_idx == col_idx:
                    curr_sum += subMatrix[row_idx][col_idx]
        summation.append(curr_sum)
        
        # check secondary diagonal
        curr_sum = 0
        for row_idx in range(row_length):
            for col_idx in range(col_length):
                if row_idx + col_idx == row_length - 1:
                    curr_sum += subMatrix[row_idx][col_idx]
        summation.append(curr_sum)
                
        if len(set(summation)) != 1:
            return False
        
        return True
        
        
        
        
        
                
                