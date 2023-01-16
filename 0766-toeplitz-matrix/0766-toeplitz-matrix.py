class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        
        row_length = len(matrix)
        col_length = len(matrix[0])
        
        # for each number check to see if the next diagonal number is equal to it or not
        for row_idx in range(row_length-1):
            for col_idx in range(col_length-1):
                
                if(matrix[row_idx][col_idx] != matrix[row_idx+1][col_idx+1]):
                    return False
                
                
        return True
                
        