class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        
        row_length = len(matrix)
        col_length = len(matrix[0])
        
        row_positions = set()
        col_positions = set()
        for row_idx in range(row_length):
            for col_idx in range(col_length):
                
                if(matrix[row_idx][col_idx] == 0):
                    row_positions.add(row_idx)
                    col_positions.add(col_idx)
                    
                    
        for row_idx in range(row_length):
            for col_idx in range(col_length):
                
                if row_idx in row_positions or col_idx in col_positions:
                    matrix[row_idx][col_idx] = 0
                                        
        

        
                    
                
                