num_laptops = int(input())
laptops = []
isHappy = False
for _ in range(num_laptops):
    
    price, quality =map(int, input().split())        
    laptops.append([price, quality])

laptops.sort()

for idx in range(len(laptops)):
    price, quality = laptops[idx] 
    if idx != 0 and laptops[idx-1][1] > quality:
        isHappy = True
        
if isHappy:
    print("Happy Alex")
else:
    print("Poor Alex")
    
     