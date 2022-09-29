class Solution:
    def maxFrequency(self, nums:List[int], k: int) -> int:
        #SORT AND SLIDING WINDOW SOLUTION
        #right pointer
        #left pointer
        #Window: list of number between out left and right pointer
        #Total: is the actual sum of the numbers in the window
        #result: is the highest frequency for a number
        nums.sort()

        left, right = 0, 0
        result, total = 0, 0

        while right < len(nums):
            total += nums[right]

            #sliding window
            while nums[right] * (right - left + 1) > total + k:
                total -= nums[left]
                left+=1
        
        result = max(result, right - left +1)
        right +=1

        return result



        
