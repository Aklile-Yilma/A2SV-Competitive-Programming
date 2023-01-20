from typing import *
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
                    
        row_bag = defaultdict(set)
        col_bag = defaultdict(set)
        sec_bag = defaultdict(set)
        
        for row_idx in range(9):
            for col_idx in range(9):
                num = board[row_idx][col_idx]

                if not num.isdigit():
                    continue

                sec = (row_idx // 3, col_idx // 3)
                if num in row_bag[row_idx] or num in col_bag[col_idx] or num in sec_bag[sec]:
                    return False
                else:
                    row_bag[row_idx].add(num)
                    col_bag[col_idx].add(num)
                    sec_bag[sec].add(num)
        
        return True