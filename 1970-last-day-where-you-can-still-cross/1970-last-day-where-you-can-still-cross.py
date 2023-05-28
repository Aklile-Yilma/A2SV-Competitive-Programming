class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        row_len, col_len = row,  col
        grid = [[0 for i in range(col)] for j in range(row)]
        inbound = lambda r, c: 0 <= r < row_len and 0 <= c < col_len 
        directions = [(1, 0), (0,1), (-1, 0), (0,-1), (1,1),(-1,-1), (1,-1), (-1,1)]
        
        uf = UnionFind(row, col)
        #union find over waters
        for idx in range(len(cells)):
            row, col = cells[idx]
            row, col = row - 1, col-1
            grid[row][col] = 1
            if col == 0:
                uf.union("left", (row, col))
            elif col == col_len - 1:
                uf.union("right", (row, col))
            
            #connect water cells 8 directionally
            for r, c in directions:
                new_row = row + r
                new_col = col + c
                if inbound(new_row, new_col) and grid[new_row][new_col] == 1:
                    uf.union((new_row, new_col), (row, col))
            
            #check if the left column is connected to right most column
            if uf.connected('left', 'right'):
                return idx
                 
        return len(cells)
                
class UnionFind:
    def __init__(self, row, col):
        self.root = {}
        self.rank = {}
        self.root["left"] = "left"
        self.rank["left"] = 0
        self.root["right"] = "right"
        self.rank["right"] = 0
        
        for r in range(row):
            for c in range(col):
                self.root[(r, c)] = (r, c)
                self.rank[(r, c)] = 0

    # Find parent of n, with path compression.
    def find(self, n):
        p = self.root[n]
        while p != self.root[p]:
            self.root[p] = self.root[self.root[p]]
            p = self.root[p]
        return p

    # Union by height / rank.
    # Return false if already connected, true otherwise.
    def union(self, n1, n2):
        root1, root2 = self.find(n1), self.find(n2)
        if root1 == root2:
            return False

        if self.rank[root1] > self.rank[root2]:
            self.root[root2] = root1
        elif self.rank[root1] < self.rank[root2]:
            self.root[root1] = root2
        else:
            self.root[root1] = root2
            self.rank[root2] += 1
        return True

    def connected(self, n1, n2):
        return self.find(n1) == self.find(n2)
