class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        prefix_sum = [0]
        prefix_sum_reversed = [0]

        for num in nums:
            prefix_sum.append(prefix_sum[-1]+num)


        for num in reversed(nums):

            prefix_sum_reversed.insert(0, num + prefix_sum_reversed[0])

#         print(prefix_sum)
#         print(prefix_sum_reversed)

        for idx, value in enumerate(nums):
            if(prefix_sum[idx] == prefix_sum_reversed[idx+1]):
                return idx

        return -1
