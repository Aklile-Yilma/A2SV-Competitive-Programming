class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        uf = UnionFind(n)
        email_map = {}
        
        for idx, acc in enumerate(accounts):
            for j in range(1, len(acc)):
                email = acc[j]
                if email in email_map:
                    uf.union(idx, email_map[email])
                else:
                    email_map[email] = idx
                
        emailGroup = defaultdict(list)
        #merge
        for email, idx in email_map.items():
            root = uf.find(idx)
            emailGroup[root].append(email)
            
        ans = []
        for idx, emails in emailGroup.items():
            ans.append([accounts[idx][0]] + sorted(emailGroup[idx]))
            
        return ans
        
class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [1] * n

    # Find parent of n, with path compression.
    def find(self, x):
        while x != self.par[x]:
            self.par[x] = self.par[self.par[x]]
            x = self.par[x]
        return x

    # Union by height / rank.
    # Return false if already connected, true otherwise.
    def union(self, x1, x2):
        p1, p2 = self.find(x1), self.find(x2)
        if p1 == p2:
            return False

        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
        elif self.rank[p1] < self.rank[p2]:
            self.par[p1] = p2
        else:
            self.par[p1] = p2
            self.rank[p2] += 1
        return True

    def connected(self, x1, x2):
        return self.find(x1) == self.find(x2)
