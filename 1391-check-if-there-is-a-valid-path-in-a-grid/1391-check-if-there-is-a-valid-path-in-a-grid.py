class Solution:
    def build(self, n):
        self.root = [node for node in range(n)]
        self.size = [1 for _ in range(n)]
        
    def find(self, x):
        #hold x
        hold = x
        while self.root[x] != x:
            x = self.root[x]
            
        #path compression
        #x is now the root, i didn't reach the root
        while x != self.root[hold]:
            temp = self.root[hold]
            #change root of node
            self.root[hold] = x
            hold = temp
            
        return x
            
    def union(self, x, y):
        root1 = self.find(x)
        root2 = self.find(y)
        size1 = self.size[root1]
        size2 = self.size[root2]
        
        if size1 <= size2:
            self.root[root2] = root1
            self.size[root1] += size2
        else:
            self.root[root1] = root2
            self.size[root2] += size1
            
    def connected(self, x, y):
        return self.find(x) == self.find(y)
    
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        
        row_len, col_len = len(grid), len(grid[0])
        self.build(row_len*col_len)
        source = [0, 0]
        destination = [row_len-1, col_len-1]
        inbound = lambda row, col: 0 <= row <  len(grid) and 0 <= col < len(grid[0])
        # up, down, left, right
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        
        #up, down, left, right
        connections = {
            1: [{}, {}, {1, 4, 6},{1, 3, 5}],
            2: [{2, 3, 4}, {2, 5, 6}, {}, {}],
            3: [{}, {2, 5, 6}, {1, 4, 6}, {}],
            4: [{}, {2, 5, 6}, [],{1, 3, 5}],
            5: [{2, 3, 4}, {}, {1, 4, 6}, {}],
            6: [{2, 3, 4}, {}, {} ,{1, 3, 5}]
        }
        visited = set()
        # k = col + (row * total_no_of_columns_in_matrix)
        for row in range(row_len):
            for col in range(col_len):
                curr_node = grid[row][col]
                visited.add((row, col))
                for idx in range(len(directions)):
                    new_row = row + directions[idx][0]
                    new_col = col + directions[idx][1]
                    if inbound(new_row, new_col) and (new_row, new_col) not in visited:
                        # print(row, col,(new_row, new_col))
                        cand_node = grid[new_row][new_col]
                        # print("nodes", curr_node, cand_node, idx)
                        if cand_node in connections[curr_node][idx]:
                            # print(self.root, (row, col), (new_row, new_col))
                            first = col + (row * col_len)
                            second = new_col + (new_row * col_len)
                            self.union(first, second)
        # print(self.root)
        return self.connected(0, row_len*col_len-1)
        
        
#         #up, down, left, right
#         #up: 2, 3, 4
#         #down: 2, 5, 6
#         #left: 1, 4, 6
#         #right: 1, 3, 5
#         connection = {
#             1: [[], [], [1, 4, 6], [1, 3, 5]],
#             2: [[2, 3, 4], [2, 5, 6], [], []],
#             3: [[], [2, 5, 6], [1, 4, 6], []],
#             4: [[], [2, 5, 6], [], [1, 3, 5]],
#             5: [[2, 3, 4], [], [1, 4, 6], []],
#             6: [[2, 3, 4], [], [], [1, 3, 5]]
#         }

        
        