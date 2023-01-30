num_neighbors = int(input())
numbers = list(map(int,input().split()))
isValid = True

numbers.sort()

if numbers[-1] >= numbers[-2] + numbers[0]:
    if numbers[-1] >= numbers[-3] + numbers[-2]:
        isValid = False
    else:
        numbers[-1], numbers[-2] = numbers[-2], numbers[-1]
    
if isValid:
    print("YES")
    print(*numbers)
    
else:
    print("NO")
    

# # print(rearranged_numbers)

# numbers = rearranged_numbers

# for idx in range(num_neighbors):
#     if idx == 0:
#         if numbers[idx] >= numbers[-1] + numbers[idx+1]:
#             isValid = False
#             break
#     if idx == num_neighbors-1:
#         if numbers[idx] >= numbers[0] + numbers[idx-1]:
#             isValid = False
#             break
#     if 0 < idx < num_neighbors-1:
#         if numbers[idx] >= numbers[idx-1] + numbers[idx+1]:
#             isValid = False
#             break