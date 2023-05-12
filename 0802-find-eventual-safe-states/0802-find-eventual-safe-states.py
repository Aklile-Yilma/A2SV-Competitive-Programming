class Solution:
	def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
		#white(0): unvisited, grey(1): visited, Black(2): done
		
		def dfs(node):
            #cycle detected return false
			if color[node] == 1:
				return False

            #not a cycle
			if color[node] == 2:
				return True

			color[node] = 1
			for child in graph[node]:
				if not dfs(child):
					return False

			color[node] = 2
			return True
		
		color = [0] * len(graph)
		return [node for node in range(len(graph)) if dfs(node)]

		