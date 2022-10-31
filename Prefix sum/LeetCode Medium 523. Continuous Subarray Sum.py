class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:

        #HashMap: {remainder: ending Index of the subarray},
        #intialize as such because for the edge case that the first element in nums is a multiple of k

        remainder = {0: -1}
        prefix = 0


        for idx, value in enumerate(nums):

            prefix += value
            curr_remainder = prefix % k

            #if curr_remainder is in remainder map that means you have added numbers to our array such that they are multiple of k
            if curr_remainder not in remainder:
                remainder[curr_remainder] = idx

            #check if it len(subarray) > 2
            elif idx - remainder[curr_remainder] > 1:
                return True


        return False

