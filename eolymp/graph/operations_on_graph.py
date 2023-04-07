from collections import defaultdict

num_verticles = int(input())
k = int(input())
graph = defaultdict(list)
for _ in range(k):
    query = list(map(int, input().split()))
    
    if query[0] == 1:
        u, v = query[1], query[2]
        graph[u].append(v)
        graph[v].append(u)
    else:
        u = query[1]
        print(*graph[u])
        

        
