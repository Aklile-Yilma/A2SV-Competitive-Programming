class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:

        row_len, col_len = len(matrix), len(matrix[0])
        
        transpose_matrix = [[0] * row_len for _ in range(col_len)]
        
        for r in range(row_len):
            for c in range(col_len):
                transpose_matrix[c][r] = matrix[r][c] 
        
        
        return transpose_matrix