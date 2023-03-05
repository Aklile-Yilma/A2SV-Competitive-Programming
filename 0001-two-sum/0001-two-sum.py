class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        
        # a map containing value: index pairs of visited nums
        
        prevMap = {}
        for idx, value in enumerate(nums):
            # the number required to fulfill our condition is target-value
            num = target - value
            if num in prevMap:
                # return the pointer of our num and current pointer
                return [prevMap[num], idx]
            
            prevMap[value] = idx