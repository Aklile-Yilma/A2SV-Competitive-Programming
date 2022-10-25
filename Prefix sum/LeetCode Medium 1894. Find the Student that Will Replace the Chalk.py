class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        

        prefix_sum = sum(chalk)
        if prefix_sum < k:
# since we don't care about the amount of iterations we will modulo k by our prefix_sum/total
            k = k%prefix_sum
        
        
        idx = 0
# help to check if idx is out of bounds
        last_idx = len(chalk) - 1

        while chalk[idx] <= k:

            value = chalk[idx]
            
            k -= value
            
            idx += 1

            if(idx > last_idx):
# reset idx if idx is out of bounds
                idx = 0


        return idx