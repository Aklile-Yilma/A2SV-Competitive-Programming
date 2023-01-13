class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        row_length = len(matrix)
        col_length = len(matrix[0])
        
        
        for row_idx in range(row_length):
            for col_idx in range(col_length):
                if(matrix[row_idx][col_idx] == target):
                    return True
                
        return False
                

# BINARY SEARCH
        
#         col = 0
#         left = 0 
#         right = row_length - 1
#         #binary search in the columns
#         while right > left:
#             middle = (right + left - 1) // 2
#             if(matrix[middle][col] <= target):
#                 right = middle
#             else:
#                 left = middle
        
#         # binary search in the rows
#         row = left
#         left = 0
#         right = col_length - 1
#         while right > left:
#             middle = (right + left - 1) // 2
#             # print(middle, left, right)
#             if(matrix[row][middle] >= target):
#                 right = middle
#                 # print("a", middle, left, right)
#             else:
#                 left = middle + 1
#                 # print("b", middle, left, right)
                
            
#         return matrix[row][right] == target
            
        
        