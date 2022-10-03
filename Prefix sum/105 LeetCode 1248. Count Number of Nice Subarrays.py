from collections import defaultdict
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        prevCount = defaultdict(int)
        prevCount[0] = 1
        res = 0
        count = 0
        for num in nums:
            if num % 2 == 1:
                count += 1
            prevCount[count] += 1
            if count - k in prevCount:
                res += prevCount[count - k]
        return res


 # doesn't count the fact that it the permuations of having even number in next to the array
#class Solution:
    #def numberOfSubarrays(self, nums: List[int], k: int) -> int:

        ## replacing even number with 0
        ## replacing odd number with 1


        #for i in range(len(nums)):
            #if(nums[i]%2 == 0):
                #nums[i] = 0
            #else:
                #nums[i] = 1

        ## making the prefix sum

        #print(nums)
        #prefix = 0
        #count = 0
        #for num in nums:
            #prefix+= num

            #if k == prefix:
                #count += 1
                #prefix-=1

        #return count
