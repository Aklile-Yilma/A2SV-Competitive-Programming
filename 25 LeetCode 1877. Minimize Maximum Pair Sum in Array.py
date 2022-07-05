class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        #Tilde operator ""~""    Index =(len(nums)-1)

        nums.sort()
        return max([nums[i]+nums[~i] for i in range(len(nums)//2)])
