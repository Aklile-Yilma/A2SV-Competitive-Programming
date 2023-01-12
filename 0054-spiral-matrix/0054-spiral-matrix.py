class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)
        while left < right and top < bottom:
            # get every i in the top row
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1
            # get every i in the right col
            for i in range (top, bottom):
                res.append(matrix[i][right - 1])
            right -= 1
            if not (left < right and top < bottom):
                break
            # get every i in the bottom row
            for i in range(right - 1, left - 1, -1):
                res.append(matrix[bottom - 1][i])
            bottom -= 1
            # get every i in the left col
            for i in range (bottom - 1, top - 1, -1):
                res.append(matrix[i][left])
            left += 1
        return res

# class Solution:
#     def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
#         spiral = []
#         row_length = len(matrix)
#         col_length = len(matrix[0])
#         cur_col, cur_row = 0, 0
#         going_down = True
#         going_right = True
#         size = row_length * col_length
#         left_boundary, top_boundary = 0, 0
        
#         #row_length is used as a bottom boundary and decremented as such
#         #col_length is used as a right boundary and decreamented as such
#         while len(spiral) < size:
            
#             if going_right or going_down:
#                 while going_right and cur_col < col_length:
#                     spiral.append(matrix[cur_row][cur_col])
#                     cur_col += 1
                    
#                 if cur_col == col_length:
#                     cur_col -= 1
#                     cur_row += 1
#                     going_right = False
                
#                 while going_down and cur_row < row_length:
#                     spiral.append(matrix[cur_row][cur_col])
#                     cur_row += 1
                    
#                 if cur_row == row_length:
#                     cur_row -= 1
#                     cur_col -= 1
#                     going_down = False
  
#             else:
#                 # going_right or going up
#                 if not going_right or not going_down:
                    
#                     while not going_right and cur_col >= left_boundary:
#                         spiral.append(matrix[cur_row][cur_col])
#                         cur_col -= 1
                        
#                     if cur_col == left_boundary-1:
#                         cur_col += 1
#                         cur_row -= 1
#                         going_right = True
#                         # shrink our bottom and left boundary
#                         col_length -= 1
#                         left_boundary += 1
                        
#                     # upto row_length -1 because the last most item has already been added
#                     while not going_down and cur_row > top_boundary:
#                         spiral.append(matrix[cur_row][cur_col])
#                         cur_row -= 1
                        
#                     if cur_row == top_boundary:
#                         cur_row += 1
#                         cur_col += 1
#                         going_down = True
#                         # shrink our top and right boundary
#                         row_length -= 1
#                         top_boundary += 1
                        
#         return spiral
        