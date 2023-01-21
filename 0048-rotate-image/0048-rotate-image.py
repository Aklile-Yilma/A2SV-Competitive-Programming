class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
#         n = len(matrix)
        
# 		# iterate through matrix
#         for i in range(n):
#             for j in range(i,n):
			
# 			    # transpose the matrix, turning rows into columns and vice versa
#                 matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
			
# 			# reverse the resulting rows
#             matrix[i].reverse()
            
            
        # list(zip(*matrix))
        
        matrix.reverse()
        n = len(matrix)
        
        for row_idx in range(n):        
            for col_idx in range(row_idx, n):
                matrix[row_idx][col_idx],matrix[col_idx][row_idx] = matrix[col_idx][row_idx], matrix[row_idx][col_idx]
                print(matrix)
                
                
        
        

        
        
        