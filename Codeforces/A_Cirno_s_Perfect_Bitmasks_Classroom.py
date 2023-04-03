num_test_cases = int(input())

for _ in range(num_test_cases):
    x = int(input())
    y = 1
    idx = 0
    while (1 << idx & x) == 0:
        idx += 1
    y = (1 << idx) 
    
    if x > y:
        print(y)
    else:
        idx = 0
        while (1 << idx & x) != 0:
            idx += 1
        y += (1 << idx)
        print(y)
