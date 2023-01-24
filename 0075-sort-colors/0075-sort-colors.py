class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
#         freq_arr= [0]*3
        
#         for value in nums:
#             freq_arr[value]+=1
                        
#         freq_idx=0
#         for idx in range(len(nums)):  
#             # move the pointer as long as we have no count value in the freq array
#             while freq_arr[freq_idx]== 0:
#                 freq_idx+=1
#             nums[idx]= freq_idx
#             freq_arr[freq_idx]-=1
                
                
                
        #another solution
        
        zeros=nums.count(0)
        ones=nums.count(1)
        twos=nums.count(2)
        idx=0
        while(zeros>0):
            nums[idx]=0
            zeros-=1
            idx+=1
        while(ones>0):
            nums[idx]=1
            ones-=1
            idx+=1
        while(twos>0):
            nums[idx]=2
            twos-=1
            idx+=1
        return nums