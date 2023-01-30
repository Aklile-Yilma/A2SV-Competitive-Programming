n_test_cases = int(input())
for _ in range(n_test_cases):
    numbers = list(map(int, input().split()))
    numbers.sort()
    
    print(numbers[1])
    
    
