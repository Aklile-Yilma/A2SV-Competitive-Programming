class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:


        # example [1,2,3,4]
        prefix = 1
        answer = []
        for num in nums:
            answer.append(prefix)
            prefix *= num

        # answer at this point [1, 1, 2, 6]

        #the next variable is called postfix but we will continue using prefix for space complexity
        prefix = 1



        for idx in reversed(range(len(nums))):
            # prefix * postfix is equal to the answer at that index
            # answer at index is equal to postfix * prefix
            answer[idx] *= prefix
            prefix *= nums[idx]

        # answer is [24, 12, 8, 6]



        return answer

