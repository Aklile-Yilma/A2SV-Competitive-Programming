class Solution:
    def printVertically(self, s: str) -> List[str]:
        
        matrix = [[letter for letter in word] for word in  s.split()]
        #create the maximum column possible
        col_length = max(len(word) for word in matrix)
        row_length = len(matrix)
        # generate a transposed matrix
        vertical_words = [["" for _ in range(row_length)] for _ in range(col_length)]

        # print(vertical_words)
        # print(matrix)
        for row_idx in range(row_length):
            for col_idx in range(col_length):
                if col_idx < len(matrix[row_idx]):
                    vertical_words[col_idx][row_idx] = matrix[row_idx][col_idx]
                else:
                    vertical_words[col_idx][row_idx] = " "
                        
        # join and remove trailing spaces 
        vertical_words = ["".join(letters).rstrip() for letters in vertical_words]
        
        return vertical_words
        
