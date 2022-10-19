class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:

        left, right , product, result = 0 , 0, 1, 0


        # iterating over our nums array
        for right, value in enumerate(nums):
            # multiply product and increament number of subarray
            product *= value

            # while product is greater than our threshold -decrease window size, decreament product, decreament total sub-array
            while product >= k and left <= right:
                product /= nums[left]
                left += 1


            if (product < k):
                # (right - left + 1) gives us all the number of combintaions in that subarray  and we add that to our result
                result += (right - left + 1)

        return result

