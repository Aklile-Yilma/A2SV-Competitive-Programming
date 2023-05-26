class Solution:
    def minDifference(self, nums: List[int]) -> int:
        
        if len(nums) <= 4:
            return 0
        
        nums.sort()
        
        #delete first three
        first_three = nums[-1] - nums[3]
        #delete last three
        last_three = nums[len(nums)-4] - nums[0]
        #delete first one and last two
        one_two = nums[len(nums)-3] - nums[1]
        #delete first two and last one
        two_one = nums[len(nums)-2] - nums[2]
        
        return min(first_three, last_three, one_two, two_one)
        
        
        

            