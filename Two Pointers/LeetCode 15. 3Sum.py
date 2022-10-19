class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:


    #sort the array so that we can you two pointer at start+1 and end
        nums.sort()

        result = []
        prev_num = []

        for idx, value in enumerate(nums):
            # left pointer pointing to the next bigger number than current num
            left = idx + 1
            right = len(nums) - 1
            required_sum = 0 - value
            curr_sum = 0

            # for the edge case that all the contiguous numbers are the same
            if(prev_num and prev_num[0] == value):
                continue
            prev_num.append(value)


            while left < right:
                curr_sum = nums[left] + nums[right]

                if(curr_sum == required_sum):
                    #value contains current value
                    answer = [value, nums[left], nums[right]]
                    # avoid duplicates
                    if not result or answer not in result:
                        result.append(answer)

                # move the right pointer because we want a smaller number than our required sum
                if(curr_sum >= required_sum):
                    right -= 1
                else:
                    # move our left pointer because we want a greater sum than we currently have
                    left += 1

        return result

