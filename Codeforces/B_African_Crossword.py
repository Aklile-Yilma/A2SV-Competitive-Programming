from collections import Counter
num_lines, num_letters = list(map(int, input().split()))

matrix = []
# taking input
for row in range(num_lines):
    matrix.append(input())
  
transpose_matrix = [ [''] * num_lines for _ in range(num_letters)]
for row in range(num_lines):
    for col in range(num_letters):
        transpose_matrix[col][row] = matrix[row][col]
   
secret_word = []  
# check rows for non-duplicates
for row in range(num_lines):
    for col in range(num_letters):
        
        #check if duplicate in row
        counter = Counter(matrix[row])
        if counter[matrix[row][col]] != 1:
            continue
        #check if duplicate in col
        counter = Counter(transpose_matrix[col])
        if counter[transpose_matrix[col][row]] != 1:
            continue
        
        secret_word.append(matrix[row][col])
        
print(''.join(secret_word))
    
        
        
