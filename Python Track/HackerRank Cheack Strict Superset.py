# Enter your code here. Read input from STDIN. Print output to STDOUT
setA= set(input().split())
n = int(input())
isSuperSet = True

for _ in range(n):
    setB = set(input().split())
    for item in setB:
        if(item not in setA):
            isSuperSet = False
            break
        
    if not isSuperSet:
        break

if(isSuperSet):
    print("True")
else:
    print("False")

    
