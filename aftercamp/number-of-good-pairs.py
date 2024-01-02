class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        
        prev = {}
        count = 0

        for num in nums:
            if num in prev:
                count += prev[num]
                prev[num] += 1
            else:
                prev[num] = 1

        return count