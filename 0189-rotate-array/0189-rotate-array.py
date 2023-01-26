class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        if k >= len(nums):
            k %= len(nums) 
            
        def swapper(left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        
        # reverse the first part of the list 
        left , right = 0, len(nums) - k - 1
        swapper(left, right)
        
        # reverse the end part of the array
        left, right = len(nums)-k, len(nums) - 1
        swapper(left, right)
        
        # reverse the whole array
        left, right = 0, len(nums)-1
        swapper(left, right)
        
        
        
#O(n)2 solution
            
#         left, right = 0, len(nums)-1
        
#         while k > 0:
#             # insert at the beginning
#             nums.insert(left, nums[right])
            
#             # remove item from the end
#             nums.pop()
            
#             # decrement k
#             k -= 1
            

    