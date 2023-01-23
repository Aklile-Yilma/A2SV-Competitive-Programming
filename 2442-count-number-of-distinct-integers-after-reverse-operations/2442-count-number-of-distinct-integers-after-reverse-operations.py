class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        
        size = len(nums)
        
        for idx in range(size):
            num_string = str(nums[idx])
            reversed_string = num_string[::-1]
            nums.append(int(reversed_string))
                                
        return len(set(nums))
            