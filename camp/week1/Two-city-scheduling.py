class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        n = len(costs)
        costs.sort(key= lambda x: x[1]-x[0])
        
        total = 0
        for idx in range(n):
            if idx < (n // 2):
                total += costs[idx][1]
            else:
                total += costs[idx][0]
                
                
        return total
