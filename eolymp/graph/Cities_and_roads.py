n = int(input())
count =0
for row in range(n):
    line = list(map(int, input().split()))
    size = len(line)
    
    for col in range(size):
        if line[col] == 1:
            count += 1
            
print(count//2)
