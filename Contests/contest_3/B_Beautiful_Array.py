# n = int(input())
# elements = list(map(int, input().split()))
# positive,  negative ,  zero = [], [], []

# for num in elements:
#     if(num > 0):
#         positive.append(num)
#     elif(num < 0):
#         negative.append(num)
#     elif(num == 0):
#         zero.append(num)

# if(len(positive) == 0):
#     num1 = negative.pop()
#     num2 = negative.pop()
#     positive.append(num1)
#     positive.append(num2)
    
# if(len(negative)%2 == 0):
#     num = negative.pop()
#     zero.append(num)
    
# print(f'{len(negative)} { " ".join(str(num) for num in negative)}')
# print(f'{len(positive)} { " ".join(str(num) for num in positive)}')
# print(f'{len(zero)} { " ".join(str(num) for num in zero)}')

from typing import *
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        row_length = 9
        col_length = 9
        
        
        def is_Repeated(self, board: List[List[str]]) -> bool:
            isRepeat = False
            
            for row_idx in range(row_length):
                curr_row = []
                for col_idx in range(col_length):
                    curr_item = board[row_idx][col_idx]

                    if board[row_idx][col_idx] in curr_row:
                        isRepeat = True
                        break

                    if curr_item.isdigit():
                        curr_row.append(curr_item)    

                if isRepeat:
                    break
                    
            return isRepeat
                
        # check if a row has duplicates
        if self.is_Repeated(board):
            return False
        
        # check if a columns has duplicates
        if self.is_Repeated(zip(*board)):
            return False
        

s = Solution()
s.isValidSudoku([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]])