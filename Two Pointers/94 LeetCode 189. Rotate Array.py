class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """



        left, right = 0, len(nums)-1

        while k > 0:
            # insert at the beginning
            nums.insert(left, nums[right])

            # remove item from the end
            nums.pop()

            # decrement k
            k -= 1


