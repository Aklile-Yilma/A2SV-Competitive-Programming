class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        
        N = len(quiet)
        graph = [[] for _ in range(N)]
        indegree = [0 for _ in range(N)]
        
        for rich, poor in richer:
            graph[rich].append(poor)
            indegree[poor] += 1
            
        q = deque()
        answer = [node for node in range(N)]
        
        for node in range(N):
            # for the most independent nodes, their can't be more richer node
            if indegree[node] == 0:
                q.append(node)
            
        while q:
            node = q.popleft()
            
            for child in graph[node]:
                indegree[child] -= 1
                #assign most quiet and richer
                if quiet[answer[child]] > quiet[node]:
                    answer[child] = node
                #assign most ancestor and richer and quiter
                if quiet[answer[child]] > quiet[answer[node]]:
                    answer[child] = answer[node]
                    
                if indegree[child] == 0:
                    q.append(child)
        
        return answer