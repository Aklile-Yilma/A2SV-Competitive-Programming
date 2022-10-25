class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
                
        nums.sort()
        n = len(nums)
        moves = 0
#         we don't need to check first element
        for i in range(1,n):
            if nums[i] <= nums[i-1]:
                # this is the case for making item unique
#                 the difference between to elements next to eachother
                diff = nums[i-1] + 1 - nums[i]
#                 numbers of moves required to make it non-duplicate == difference
                moves += diff
#               value of of current element = value of previous element + 1
#               3 = 7 + 1
                nums[i] = nums[i-1] + 1
        return moves