class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        
        graph = [[] for _ in range(n)]
        counts = [0] * n
        
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
                        
        def merge_dictionary(dict_1, dict_2):
            dict_3 = {**dict_1, **dict_2}
            for key, value in dict_3.items():
                if key in dict_1 and key in dict_2:
                    dict_3[key] = value + dict_1[key]
            return dict_3

        def dfs(node, parent, letters_count):
            if graph[node] == []:
                letters_count[labels[node]] = letters_count.get(labels[node], 0) + 1
                counts[node] = letters_count.get(labels[node], 0) 
                return letters_count
            
            for child in graph[node]:
                if child != parent:
                    letters_count = merge_dictionary(letters_count, dfs(child, node, {}))
                
            letters_count[labels[node]] = letters_count.get(labels[node], 0) + 1
            counts[node] = letters_count[labels[node]]
            
            return letters_count
        
        dfs(0, -1, {})

        return counts
            
        