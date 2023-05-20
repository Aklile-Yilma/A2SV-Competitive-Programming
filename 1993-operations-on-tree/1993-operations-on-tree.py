class LockingTree:

    def __init__(self, parent: List[int]):
        size = len(parent)
        self.root = 0
        self.parent = parent
        self.decendant = [[] for node in range(size)]
        self.status = [-1 for _ in range(size)]
        for node in range(1, size):
            p = parent[node]
            self.decendant[p].append(node)
                    
    def lock(self, num: int, user: int) -> bool:
        if self.status[num] == -1: 
            self.status[num] = user
            return True
        
        return False

    def unlock(self, num: int, user: int) -> bool:
        if self.status[num] == user:
            self.status[num] = -1
            return True

        return False
        
    def upgrade(self, num: int, user: int) -> bool:
        # print(num, self.status)
        if self.status[num] != -1:
            return False

        #check if all ancestors not locked
        def dfs(node):
            if self.status[node] != -1:
                return False
            
            if node == self.root:
                return True

            return dfs(self.parent[node])

        if not dfs(num):
            return False
        
        #check if atleast one locked descendant
        found = False
        visited = set()
        def dfs(node):
            nonlocal found

            if self.status[node] != -1:
                found = True
                self.status[node] = -1

            visited.add(node)
            for child in self.decendant[node]:
                if child not in visited:
                    dfs(child)

            return
        
        dfs(num)

        #if it has a locked descendant
        if found:
            self.status[num] = user
            return True

        return False

# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)