class Solution:
    def __greaterDigit(self,num1, num2):
        num3= num1 + num2
        num4= num2 + num1
        
        return -1 if (num3 > num4) else 1
        
        
    def largestNumber(self, nums: List[int]) -> str:
        for i, value in enumerate(nums):
            nums[i]= str(value)
        
        nums=sorted(nums, key=functools.cmp_to_key(self.__greaterDigit))
        
        return str(int(''.join(nums)))
        