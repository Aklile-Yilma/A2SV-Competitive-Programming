n_test_cases = int(input())
is_replaceable = True

for _ in range(n_test_cases):
    length = int(input())
    numbers = map(int, input().split())
    letters = input()
    
    numbers_map = {}
    
    for number, letter in zip(numbers, letters):
        if number in numbers_map:
            if(numbers_map[number] != letter):
                is_replaceable = False
                break
        
        else:
            numbers_map[number] = letter
    
    if is_replaceable: 
        print("YES")
    else: 
        print("NO")
        
    is_replaceable = True
        
    
