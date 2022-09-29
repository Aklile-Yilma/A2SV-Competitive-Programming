import math
n, m, a = map(float, input("").split(" "))

flagstones_in_width= math.ceil(n/a)
flagstones_in_height = math.ceil(m/a)

Total_flagstones = flagstones_in_width * flagstones_in_height 

print(Total_flagstones)




