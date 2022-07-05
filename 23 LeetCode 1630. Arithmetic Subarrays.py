from typing import *

class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        
        IsArthimetic_list = []
        IsArthimetic = True
        
        for i,j in zip(l,r):
            s= slice(i,j)
            numbers= nums[slice(i,j+1)]
            
            numbers.sort()
            
            constant = numbers[1]- numbers[0]
            for k in range(len(numbers)):
                if(k == (len(numbers)-1)):
                    break
                if( (numbers[k+1]- numbers[k]) != constant):
                    IsArthimetic = False
                    break

            IsArthimetic_list.append(IsArthimetic)
            IsArthimetic=True


        return IsArthimetic_list


s= Solution()
print(s.checkArithmeticSubarrays([4,6,5,9,3,7], [0,0,2], [2,3,5]))

