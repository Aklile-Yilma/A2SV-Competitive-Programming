# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        
        if k == 0:
            return [target.val]
        
        graph = defaultdict(list)
        q = deque()
        q.append(root)
        
        while q:
            node = q.popleft()
            if node.left:
                graph[node.val].append(node.left.val)
                graph[node.left.val].append(node.val)
                q.append(node.left)
            
            if node.right:
                graph[node.val].append(node.right.val)
                graph[node.right.val].append(node.val)
                q.append(node.right)
        
        visited = {target.val}
        q = deque()
        q.append((target.val, 0))
        answer = []
                
        while q:
            size = len(q)
    
            for _ in range(size):
                node, dist = q.popleft()
                
                if dist == k:
                    answer.append(node)
                    
                for child in graph[node]:
                    if child not in visited:
                        visited.add(child)
                        q.append((child, dist + 1))
                        
                if dist > k:
                    break
                
        return answer
                    
        