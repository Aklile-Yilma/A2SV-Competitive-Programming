# Enter your code here. Read input from STDIN. Print output to STDOUT
sizes = input().split()
array = input().split()
set_A = set(input().split())
set_B = set(input().split())


happiness = 0


for num in array:
    if(num in set_A): happiness += 1
    elif(num in set_B): happiness -= 1

        
print(happiness)
