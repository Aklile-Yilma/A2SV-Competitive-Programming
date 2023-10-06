class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        
        memo = {}
        n = len(stones)
        target = sum(stones) // 2
        
        def dfs(idx, curr_sum):
            
            if idx >= n:
                return curr_sum
            
            if (idx, curr_sum) not in memo:
                pick = dfs(idx+1, curr_sum + stones[idx])
                not_pick = dfs(idx+1, curr_sum)
            
                memo[(idx, curr_sum)] = pick if abs(target - pick) < abs(target - not_pick) else not_pick
        
            return memo[(idx, curr_sum)]
        
        first_bucket = dfs(0, 0)
        second_bucket = sum(stones) - first_bucket
        
        return abs(first_bucket - second_bucket)