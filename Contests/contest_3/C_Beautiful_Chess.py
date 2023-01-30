num_test_cases = int(input())

col_length = 8
row_length = 8


for _ in range(num_test_cases):
    num_tag = []
    input()
    for _ in range(col_length):
        count = 0
        col_idx = -1
        row = input()
        for idx, char in enumerate(row):
            if char == '#':
                count += 1
                col_idx = idx
                
        num_tag.append((col_idx, count))

    row = -1
    for idx in range(1, len(num_tag)-1):
        value = num_tag[idx][1]
        if value == 1 and num_tag[idx-1][1] == 2:
            row = idx+1
            col = num_tag[idx][0]+1
            print(row,col)
            break
    
            
        
    
        

                

                
                
                
    
    