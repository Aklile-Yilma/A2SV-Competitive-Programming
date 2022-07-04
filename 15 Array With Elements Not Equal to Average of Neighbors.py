#1968. Array With Elements Not Equal to Average of Neighbors
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        result=[]

        left, right= 0, len(nums)-1
        while len(result) != len(nums):
            result.append(nums[left])
            left+=1

            if(left<=right):
                result.append(nums[right])
                right-=1

        return result

