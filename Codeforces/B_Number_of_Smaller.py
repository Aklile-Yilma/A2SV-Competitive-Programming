n, m = map(int, input().split())
first_arr = list(map(int, input().split()))
second_arr = list(map(int, input().split()))

smaller_counts = []

first_ptr = 0
for second_ptr in range(len(second_arr)):
    
    while first_ptr < n and first_arr[first_ptr] < second_arr[second_ptr]:
        first_ptr += 1
        
    smaller_counts.append(first_ptr)
    
print(*smaller_counts)