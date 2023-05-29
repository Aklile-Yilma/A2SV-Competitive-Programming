class Solution:
    def __init__(self):
        self.memo = {}
        
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        
        size = len(coins)
        coins.sort(reverse=True)
        
        #remaining amount, seqence_length
        q = deque()
        
        for idx in range(size):
            coin = coins[idx]
            curr_total = amount - coin
            if coin <= amount and curr_total not in self.memo:
                q.append((curr_total, 1))
                self.memo[curr_total] = 1
                
        while q:
            remaining, steps = q.popleft()
            if remaining == 0:
                return steps
            
            for idx in range(size):
                coin = coins[idx]
                curr_total = remaining - coin
                
                if curr_total >= 0 and curr_total not in self.memo:
                    q.append((curr_total, steps+1))
                    self.memo[curr_total] = steps + 1
                    
        return -1