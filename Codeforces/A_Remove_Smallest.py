num_testcases = int(input())

for _ in range(num_testcases):
    size = int(input())
    numbers = list(map(int, input().split()))
    numbers.sort()
    isValid = True
    left = 0
    
    for right in range(1, size):
        
        if abs(numbers[left] - numbers[right]) > 1:
            isValid = False
            break
        
        left += 1
        
    if isValid:
        print("YES")
    else:
        print("NO")
    
