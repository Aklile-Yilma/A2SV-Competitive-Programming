class Solution:
    def longestSubarray(self, nums: List[int]) -> int:

        left = 0
        result, total = 0, 0
        #determines the number of 0
        k = 0

        for right,num in enumerate(nums):

            # increamenting total by 1 if num is 1
            total += num

            # decreamenting k by 1 if num is 0
            k += (num - 1)


            if(k <= -2):
                while nums[left] and nums[left] != 0:
                    # decreamenting one because we are removing 1's from the window
                    total -=1
                    left += 1

                # decreament total if left most window was zero
                left += 1
                k += 1


            result = max(result, total)

        return result if k != 0 else result - 1
