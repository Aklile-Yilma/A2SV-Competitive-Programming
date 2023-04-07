from collections import defaultdict

n = int(input())
graph = defaultdict(list)

for row in range(n):
    line = list(map(int, input().split()))
    size = len(line)
    
    for col in range(size):
        if line[col] == 1:
            graph[row+1].append(col+1)
    
for node in graph:
    children = graph[node]
    print(len(children), *children)
    
