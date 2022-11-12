class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        prefix_sum = [0]
        suffix_sum = [0]

        for num in nums:
            prefix_sum.append(prefix_sum[-1]+num)


        for num in reversed(nums):
            suffix_sum.insert(0, num + suffix_sum[0])



        for idx, value in enumerate(nums):
            if(prefix_sum[idx] == suffix_sum[idx+1]):
                return idx

        return -1
