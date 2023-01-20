class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
#         row_length = 9
#         col_length = 9
        
        
#         #iterate through rows
#         for row_idx in range(row_length):
#             isRepeated = False
#             curr_row = []
#             for col_idx in range(col_length):
#                 curr_board[row_idx][col_idx]
                
#                 if board[row_idx][col_idx] in curr_row:
#                     isRepeated = True
#                     break
#                 curr_row.append()    
                
#             if isRepeated:
#                 break
                
                
                
                
                
            
        row_bag = defaultdict(set)
        col_bag = defaultdict(set)
        sec_bag = defaultdict(set)
        
        for i in range(9):
            for j in range(9):
                num = board[i][j]

                if not num.isdigit():
                    continue

                sec = (i // 3, j // 3)
                if num in row_bag[i] or num in col_bag[j] or num in sec_bag[sec]:
                    return False
                else:
                    row_bag[i].add(num)
                    col_bag[j].add(num)
                    sec_bag[sec].add(num)
        return True