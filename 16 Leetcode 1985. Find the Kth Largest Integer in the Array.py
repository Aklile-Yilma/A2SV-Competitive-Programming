class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
            nums.sort(key = int)
            return nums[len(nums)-k]

