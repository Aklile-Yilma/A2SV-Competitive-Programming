from typing import List


class Solution:
    # Function to detect cycle in an undirected graph.
    def isCycle(self, V: int, adj: List[List[int]]) -> bool:
        # Code here

        def dfs(node, parent):

            visited.add(node)
            for child in adj[node]:
                if child == parent:
                    continue
                # found cycle
                if child in visited:
                    return True
                if dfs(child, node):
                    return True

            return False

        visited = set()
        for node in range(v):
            if node not in visited:
                if dfs(node, -1):
                    return 1

        return 0

                
		      


#{ 
 # Driver Code Starts
if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isCycle(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends