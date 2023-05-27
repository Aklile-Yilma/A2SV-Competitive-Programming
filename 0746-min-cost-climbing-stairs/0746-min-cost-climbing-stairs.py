class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        self.memo = {}
        def recursion(idx):
            nonlocal cost
            if idx == len(cost)-1 or idx == len(cost)-2:
                return cost[idx]
            
            if idx not in self.memo:
                self.memo[idx] = [recursion(idx+1), recursion(idx+2)]
                
            return cost[idx] + min(self.memo[idx])
            
        return min(recursion(0), recursion(1))