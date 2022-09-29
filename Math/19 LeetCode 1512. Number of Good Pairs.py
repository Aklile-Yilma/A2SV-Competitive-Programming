 
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:

        pairs = []

        for i in range(len(nums)):
            for j in range(i+1, len(nums), 1):

                if(nums[i] == nums[j]):
                    print(j)
                    pairs.append((nums[i], nums[j]))

        return len(pairs)


#O(n) Solution

#class Solution:
    #def numIdenticalPairs(self, nums: List[int]) -> int:

        #counts = Counter(nums)
        #res = 0
        #for v in counts.values():
            #if v > 1:
                #res += v * (v - 1) // 2

        #return res
