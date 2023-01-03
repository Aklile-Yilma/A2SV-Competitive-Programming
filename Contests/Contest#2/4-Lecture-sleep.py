num_minutes, k = map(int, input().split())

theorems = list(map(int,input().split()))
sleep_behaviour = list(map(int,input().split()))

#max_theorem without waking him up
max_theorem = 0

for theorem, sleep in zip(theorems, sleep_behaviour):
    max_theorem += (sleep * theorem)   

left = 0
# maximum you can achieve when waking him up
max_trick_theorems = 0
#curr trick theorem in window size k
trick_theorems = 0

for right, num in enumerate(sleep_behaviour):
        # if he is asleep
    if(num == 0):
        trick_theorems += theorems[right]
        
    if(right-left+1 == k):
        max_trick_theorems = max(max_trick_theorems, trick_theorems)
        if(sleep_behaviour[left] == 0):
            trick_theorems -=  theorems[left]
        left+=1

print(max_trick_theorems + max_theorem)
    
        
