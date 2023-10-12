class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        if sum(gas) < sum(cost):
            return -1

        n = len(gas)
        total = 0
        idx = 0
        
        for i in range(n):
            total += gas[i] - cost[i]
            if total < 0:
                total = 0
                idx = i + 1
                
        return idx
                
            
        