size = int(input())
numbers = list(map(int, input().split()))
left, right = 0, 0
isFirst = False
for right, num in enumerate(numbers):
    if not isFirst and right+1 < len(numbers) and numbers[right] > numbers[right+1]: 
        left = right
        isFirst = True
    elif isFirst and right+1 < len(numbers) and numbers[right] < numbers[right+1]:
        break
    
    
left_idx = left + 1
right_idx = right + 1   
while isFirst and left < right:
    numbers[left], numbers[right]= numbers[right], numbers[left]
    left+=1
    right-=1
    
if sorted(numbers) == numbers:
    print("yes")
    if isFirst:
        print(left_idx, right_idx)
    else:
        print(1, 1)
else:
    print("no")         
