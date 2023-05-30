class Solution:
    def maximumSegmentSum(self, nums: List[int], removeQueries: List[int]) -> List[int]:
        n = len(nums)
        inbound = lambda idx: 0 <= idx < n 
        rev_nums = [-1] * n

        uf = UnionFind(n, nums)        
        curr_max = 0
        ans = [0]
        #reverse union find
        for idx in reversed(removeQueries):
            rev_nums[idx] = nums[idx]
            
            left = idx - 1
            right = idx + 1
            
            if inbound(left) and rev_nums[left] != -1:
                uf.union(idx, left)
            
            if inbound(right) and rev_nums[right] != -1:
                uf.union(idx, right)
            
            #find curr_max sum
            curr_max = max(curr_max, uf.max_sum[uf.find(idx)])  
            ans.append(curr_max)
           
        ans.pop()
        ans.reverse()
        
        return ans
        
class UnionFind:
    def __init__(self, n, nums):
        self.root = {}
        self.rank = {}
        self.max_sum = {}

        for i in range(n):
            self.root[i] = i
            self.max_sum[i] = nums[i]
            self.rank[i] = 0

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
            self.max_sum[root1] += self.max_sum[root2]
        elif self.rank[root1] < self.rank[root2]:
            self.root[root1] = root2
            self.max_sum[root2] += self.max_sum[root1]
        else:
            self.root[root1] = root2
            self.rank[root2] += 1
            self.max_sum[root2] += self.max_sum[root1]
            
        return True

    def connected(self, n1, n2):
        return self.find(n1) == self.find(n2)