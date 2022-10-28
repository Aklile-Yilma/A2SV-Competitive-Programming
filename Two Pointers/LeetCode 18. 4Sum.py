from typing import *
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        nums.sort()

        for first_idx, first_num in enumerate(nums):
            # used to pick the second number other than the current number
            for second_idx, second_num in enumerate(nums[first_idx+1:]):

                # left = first_idx + second_idx + 2 because we are accessing the actual list not the sliced list and its zero indexed
                left = first_idx + second_idx + 2
                right = len(nums) - 1
                # picking two pairs of numbers, one current value and another one
                required_sum = target - first_num - second_num
                curr_sum = 0


                while left < right:
                    curr_sum = nums[left] + nums[right]

                    if(curr_sum == required_sum):
                        answer = (first_num, second_num, nums[left], nums[right])
                        if not result or answer not in result:
                            result.append(answer)


                    if(curr_sum >= required_sum):
                        right -= 1
                    else:
                        left += 1


        return result





s = Solution()
print(s.fourSum([1,0,-1,0,-2,2], 0))


