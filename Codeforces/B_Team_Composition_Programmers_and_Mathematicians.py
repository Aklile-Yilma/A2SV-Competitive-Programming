num_test_cases = int(input())

def isPosssible(num_programmers, num_maths, mid):
    
    if mid == 0:
        return True
    
    a = num_programmers//mid
    b = num_maths // mid
    
    if a>= 1 and b >= 1 and (num_programmers+num_maths)// mid>= 4:
        return True
    
    return False

    

for _ in range(num_test_cases):
    num_programmers, num_maths = list(map(int, input().split()))
    search_space = min(num_programmers, num_maths)
    
    low= 0 
    high = search_space
    while low <= high:
        mid = (low + high) // 2

        if isPosssible(num_programmers, num_maths, mid):
            low = mid + 1
        else:
            high = mid - 1
            
    print(high) 
    
