class NumArray:

    def __init__(self, nums: List[int]):
        self.nums  = nums
        #initializing the array as zero to help get the first range sum which will always be 0 + the first element in the nums array
        self.prefix = [0]
        
        #iterating through nums summing each element to previous cumulative sum
        for num in self.nums: 
            self.prefix.append(self.prefix[-1]+num)

    def sumRange(self, left: int, right: int) -> int:
        
        return self.prefix[right + 1] - self.prefix[left]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)