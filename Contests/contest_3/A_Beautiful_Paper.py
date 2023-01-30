num_test_cases = int(input())

for _ in range(num_test_cases):
    side1, side2 = map(int, input().split())
    side3, side4 = map(int, input().split())
    
    if(side1 == side3):
        if(side2 + side4 == side1):
            print("Yes")
            continue
    
    if(side1 == side4):
        if(side2 + side3 == side1):
            print("Yes")
            continue
    
    if(side2 == side3):
        if(side1 + side4 == side2):
            print("Yes")
            continue
    
    if(side2 == side4):
        if(side1 + side3 == side2):
            print("Yes")
            continue
    
    print("No")
        
        
