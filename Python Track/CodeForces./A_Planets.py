from collections import Counter
n = int(input())

for _ in range(n):
    num_planets, cost_second_machines= list(map(int,input().split()))
    orbits = list(map(int, input().split()))
    
    # map of key value pairs of {orbit :  number of planets}
    orbits_map = Counter(orbits)
    
    cost = 0
    for orbit_num in orbits_map:
        
        num_of_planets = orbits_map[orbit_num]
        # if the number planets at one orbit is greater than the cost of the second machine: use the second machine
        if(num_of_planets >= cost_second_machines):
            cost += cost_second_machines
            
        else:
            # use the first machine 
            cost += num_of_planets
    
    print(cost)
    
