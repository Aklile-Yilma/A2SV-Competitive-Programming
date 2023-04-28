class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        q = deque()
        q.append(0)
        visited = {0}
        
        
        while q:
            room = q.popleft()
            keys = rooms[room]
            
            for key in keys:
                if key not in visited:
                    visited.add(key)
                    q.append(key)
                    
        return True if len(visited) == n else False

            