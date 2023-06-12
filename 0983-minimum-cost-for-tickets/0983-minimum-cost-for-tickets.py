class Solution:
    def __init__(self):
        self.memo = {}
        
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        
        
        def dfs(curr_idx):
            
            if curr_idx == len(days):
                return 0
            
            if curr_idx not in self.memo:
                self.memo[curr_idx] = float('inf')
                
                for d, c in zip([1, 7, 30], costs):
                    #find next index
                    j = curr_idx
                    while j < len(days) and days[j] < days[curr_idx] + d:
                        j += 1
                        
                    self.memo[curr_idx] = min(self.memo[curr_idx], c + dfs(j))
                
            return self.memo[curr_idx]
        
        return dfs(0)