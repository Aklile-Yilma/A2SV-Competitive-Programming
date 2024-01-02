class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        nums = set(arr)
        k_miss_count = 0

        for idx in range(1, 2001):
            if idx not in nums:
                k_miss_count += 1

            if k_miss_count == k:
                return idx

        return -1