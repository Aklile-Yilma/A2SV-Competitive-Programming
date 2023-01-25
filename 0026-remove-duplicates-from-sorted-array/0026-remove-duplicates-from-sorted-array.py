class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        holder = 0
        for seeker in range(1, len(nums)):
            if nums[holder] != nums[seeker]:
                holder+=1
                nums[holder] = nums[seeker]
                
        return holder+1
