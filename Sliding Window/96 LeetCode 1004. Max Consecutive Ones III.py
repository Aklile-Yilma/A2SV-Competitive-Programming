class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:


        left = 0
        #right pointer iterating through nums
        for right, num in enumerate(nums):

            # k is decreased when zero is found
            if(num == 0):
                k-=1

            #when k is less than zero then our window is no longer valid so we move our left pointer
            if(k < 0):
                # incrementing k if we had a zero as our first element in our window
                k += (1-nums[left])
                left +=1

        return right-left + 1
