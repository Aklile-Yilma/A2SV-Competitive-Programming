n , m = map(int, input().split())
first_arr = list(map(int, input().split()))
second_arr = list(map(int, input().split()))
size = n + m
third_arr = []
 
first_pointer, second_pointer = 0, 0
 
 
while first_pointer < n and second_pointer < m:
    
    if first_arr[first_pointer] <= second_arr[second_pointer]:
        third_arr.append(first_arr[first_pointer])
        first_pointer += 1
    else:
        third_arr.append(second_arr[second_pointer])
        second_pointer += 1        
 
third_arr += first_arr[first_pointer:]
third_arr += second_arr[second_pointer:]
        
print(*third_arr)
        
        
    
        
        
    
