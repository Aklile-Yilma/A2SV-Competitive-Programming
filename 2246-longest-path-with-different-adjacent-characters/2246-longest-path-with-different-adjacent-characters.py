class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        
        n = len(s)
        graph = [[] for _ in range(n)] 
        
        for node in range(1, n):
            p = parent[node]
            graph[p].append(node)
            
        longestPath = 0
        
        def dfs(node):
            nonlocal longestPath
            
            firstLongestChain = 0
            secondLongestChain = 0
            
            for child in graph[node]:
                char, curr_longest = dfs(child) 
                
                if char != s[node]:
                    if curr_longest >= firstLongestChain:
                        secondLongestChain = firstLongestChain
                        firstLongestChain = curr_longest
                    elif curr_longest > secondLongestChain:
                        secondLongestChain = curr_longest
                        
            longestPath = max(longestPath, firstLongestChain + secondLongestChain + 1)
            
            return s[node], firstLongestChain + 1
        
        dfs(0)
        
        return longestPath
            