class NumMatrix:

    def __init__(self, matrix: List[List[int]]):

        #getting row and col size of the matrix
        ROWS, COLS = len(matrix), len(matrix[0])
        #creating our sum matrix with offset of 1 in both col and row
        self.sumMat = [[0] * (COLS + 1) for r in range(ROWS + 1)]

        for r in range(ROWS):
            prefix = 0
            for c in range(COLS):
                #summing the row values by moving through the cols
                prefix += matrix[r][c]
                #getting the above (row, col) matrix value
                above = self.sumMat[r][c + 1]
                #setting our current value
                self.sumMat[r + 1] [c + 1] = prefix + above


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # adding the offset by 1
        r1, c1, r2, c2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1

        #bottomRight contains all the prefix sum up to that [row][col]
        bottomRight = self.sumMat[r2][c2]
        #above contains the sum above outside our box
        above = self.sumMat[r1 - 1][c2]
        #left contains the sum left to our box
        left = self.sumMat[r2][c1 - 1]
        #topleft is the number at the topleft of our box and it will be substracted twice so we add it back once
        topLeft = self.sumMat[r1 - 1][c1 - 1]

        return bottomRight - above - left + topLeft



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
