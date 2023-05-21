from collections import deque
def parallelCourses(n, prerequisites):
    # Write your code here.
    graph = [[] for _ in range(n+1)]
    indegree = [0 for _ in range(n+1)]
    for u, v in prerequisites:
        graph[u].append(v)
        indegree[v] += 1

    q = deque()
    visited = set()

    #collect independent nodes
    for node in range(1, n+1):
        if indegree[node] == 0:
            q.append(node)
            visited.add(node)

    semesters = 0
    while q:
        size = len(q)
        for _ in range(size):
            node = q.popleft()

            for child in graph[node]:
                indegree[child] -= 1
                if indegree[child] == 0:
                    q.append(child)
                    visited.add(child)
        semesters += 1

    if len(visited) != n:
        return -1

    return semesters
