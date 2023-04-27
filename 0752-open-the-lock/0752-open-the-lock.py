class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        if "0000" in deadends:
            return -1
        
        def get_neighbors(node):
            node_list = list(node)
            children_list = []
            
            for i in range(len(node)):
                curr = node_list[i]
                nxt = str((int(curr) + 1)%9)
                children_list.append(''.join(node_list[:i] + [nxt] + node_list[i+1:]))
                prev = "9" if curr == '0' else str(int(curr) - 1)
                children_list.append(''.join(node_list[:i] + [prev] + node_list[i+1:]))
        
            return children_list
        
        q = deque()
        q.append(('0000', 0))
        visited = {'0000'}
        
        while q:
            node, step = q.popleft()
            if node == target:
                return step
            
            children = get_neighbors(node)
            for child in children:
                if child not in deadends and child not in visited:
                    visited.add(child)
                    q.append((child, step + 1))
                    
        return -1
        
        
        

        
        