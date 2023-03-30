size = int(input())
numbers = list(map(int, input().split()))

isOdd, isEven = False, False
for num in numbers:
    if num % 2 == 0:
        isEven = True
    else:
        isOdd = True

if isOdd and isEven:
    numbers.sort()
    print(*numbers)        
else:
    print(*numbers)
