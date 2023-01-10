class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
                        
        even_sum = sum(value for value in nums if value % 2 == 0)
        
        res = []

        for val, idx in queries:
            # remove the number from prefix even sums if it's even
            if nums[idx] % 2 == 0:
                even_sum -= nums[idx]
            
            #add val
            nums[idx] += val
            
            # if the number is still even or new even add it to prefix sum
            if nums[idx] % 2 == 0:
                even_sum += nums[idx]
            
            res.append(even_sum)
        
        return res
            
        