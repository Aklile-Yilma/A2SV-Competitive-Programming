class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        
        row_length = len(mat)
        col_length = len(mat[0])
        
        if row_length * col_length != r * c:
            return mat
        
        new_mat = [['' for i in range(c)] for i in range(r)]
        flatten_list = [col for row in mat for col in row]        
        idx = 0
        for row_idx in range(r):
            for col_idx in range(c):
                new_mat[row_idx][col_idx] = flatten_list[idx]
                idx += 1
                    
        return new_mat
    
# class Solution:
#     def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:  
    
#         row_length = len(mat)
#         col_length = len(mat[0])
        
#         if row_length * col_length != r * c:
#             return mat
        
#         new_mat = [['' for i in range(c)] for i in range(r)]
        
#         idx = 0
#         for row_idx in range(row_length):
#             for col_idx in range(col_length):
#                 new_mat[idx//c][idx%c] = mat[row_idx][col_idx]
#                 idx += 1

            
#         return new_mat 
        
        
        
        
        
        