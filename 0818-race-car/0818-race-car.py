class Solution:
    def racecar(self, target: int) -> int:

        def addToQ(q, cand, visited):
                if cand not in visited:
                    q.append(cand)
                    visited.add(cand)

                return
        step = 0
        position = 0
        speed = 1

        q = deque()
        #position, speed
        q.append((position, speed))
        q.append((position, speed))
        

        visited = {(0, 1), (0, 1)}
        while q:
            size = len(q)
            for _ in range(size):
                position, speed = q.popleft()
                if position == target:
                    return step

                cand = (position+speed, speed*2)
                if cand not in visited:
                    q.append(cand)
                    visited.add(cand)
                    
                if speed > 0:
                    cand = (position, -1)
                    if cand not in visited:
                        q.append(cand)
                        visited.add(cand)
                else:
                    cand = (position, 1)
                    if cand not in visited:
                        q.append(cand)
                        visited.add(cand)

            step += 1
        


