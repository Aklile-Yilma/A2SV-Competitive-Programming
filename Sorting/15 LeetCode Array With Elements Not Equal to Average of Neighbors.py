class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:

        # Algorithm: to guarantee that an element is not an average of its  #Neighbors then we just need to make sure that the numbers are both #above it or both below it
        # we skip through and add the first half element by jumping one index and we add add the second values in between the jumped spots
        # nums -> [1, 2, 3 , 4, 5]
        # result -> [1, _, 2, _, 3]
        # result -> [1, 4, 2, 5, 3]
        nums.sort()
        result=[]



        left, right= 0, len(nums)-1
        while len(result) != len(nums):
            result.append(nums[left])
            left+=1

            #if its an odd number of elements
            if(left<=right):
                result.append(nums[right])
                right-=1

        return result

