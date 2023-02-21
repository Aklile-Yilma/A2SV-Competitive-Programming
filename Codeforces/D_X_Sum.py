num_test_cases = int(input())


for _ in range(num_test_cases):
    num_lines, num_integers = list(map(int, input().split()))
    
    #get board
    board = []
    for _ in range(num_lines):
        line = list(map(int, input().split()))
        board.append(line)
        

    # along main diagonal
    main_diagonal = {}
    
    for start_row in range(num_lines-1, -1, -1):
        start_col = 0
        col = 0
        curr_sum = 0
        row = start_row
        while row < num_lines and col < num_integers:
            curr_sum += board[row][col]
            row += 1
            col += 1
        main_diagonal[start_row-start_col] = curr_sum
        
    for start_col in range(1, num_integers):
        start_row = 0
        row = 0
        col = start_col
        curr_sum = 0
        while row < num_lines and col < num_integers:
            curr_sum += board[row][col]
            row += 1
            col += 1
        main_diagonal[start_row-start_col] = curr_sum
        
    # along secondary diagonal
    secondary_diagonal = {}
    
    for start_col in range(num_integers-1, -1, -1):
        col = start_col
        curr_sum = 0
        start_row = num_lines - 1
        row = start_row
        while row >= 0 and col < num_integers:
            curr_sum += board[row][col]
            row -= 1
            col += 1
            
        secondary_diagonal[start_row+start_col] = curr_sum
        
    for start_row in range(0, num_lines-1):
        start_col = col = 0
        curr_sum = 0
        row = start_row
        
        while row >= 0 and col < num_integers:
            curr_sum += board[row][col]
            row -= 1
            col += 1
        secondary_diagonal[start_row+start_col] = curr_sum
    
    #get max diagonal sum
    max_sum = 0    
    # find max sum
    for row in range(num_lines):
        for col in range(num_integers):
            # substract doubled sum
            max_sum = max(max_sum, main_diagonal[row-col] + secondary_diagonal[row+col] - board[row][col])
            
    print(max_sum)
    
                            
    
    

            
                
            
    
    
    

    
    
    
