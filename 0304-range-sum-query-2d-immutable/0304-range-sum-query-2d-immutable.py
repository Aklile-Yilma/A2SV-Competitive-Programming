class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        
        self.matrix = matrix
        self.row = len(self.matrix)
        self.col = len(self.matrix[0])
        self.row_prefix = self.row + 1
        self.col_prefix = self.col + 1
        self.prefix = [ [0] * self.col_prefix for _ in range(self.row_prefix)]
        
        for i in range(self.row):
            for j in range(self.col):
                self.prefix[i+1][j+1] = self.prefix[i][j+1] + self.prefix[i+1][j] + self.matrix[i][j] - self.prefix[i][j]
                

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        
        total_sum = self.prefix[row2+1][col2+1]
        left_sum = self.prefix[row2+1][col1]
        top_sum = self.prefix[row1][col2+1]
        diagonal_sum = self.prefix[row1][col1]
        
        return total_sum - left_sum - top_sum + diagonal_sum
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)