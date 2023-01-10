class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:

            
        row_length = len(mat)
        col_length = len(mat[0])
        res = []
        cur_row = cur_col = 0
        
        going_up = True
        
        while len(res) < row_length * col_length:
            if going_up:
                while cur_row >= 0 and cur_col < col_length:
                    res.append(mat[cur_row][cur_col])
                    
                    # going upper
                    cur_row -= 1
                    cur_col += 1
                
                # when we are out of bounds at the highest edge we need to move down twice and turn left
                if cur_col == col_length:
                    cur_col -= 1
                    cur_row += 2
                else:
                    # turn left
                    cur_row += 1
                
                going_up = False
            else:
                while cur_row < row_length and cur_col >= 0:
                    res.append(mat[cur_row][cur_col])
                    
                    # going down
                    cur_col -= 1
                    cur_row += 1
                    
                # when we are out of bounds at the highest edge we need to move up twice and turn right            
                if cur_row == row_length:
                    cur_col += 2
                    cur_row -= 1
                else:
                    # turn right
                    cur_col += 1
                
                going_up = True
        
        return res
            
        
        
        