n , k = list(map(int, input().split()))
numbers = list(map(int, input().split()))

#sort the numbers
numbers.sort()
    
x = numbers[k-1]
if k != n: 
    x2 = numbers[k]

if k == n:
    print(x)
elif k == 0 and numbers[0] != 1:
    print('1')
elif k == 0:
    print('-1')
elif x == x2 or x < 1 or x > 10**9:
    print("-1")
else:
    print(x)
