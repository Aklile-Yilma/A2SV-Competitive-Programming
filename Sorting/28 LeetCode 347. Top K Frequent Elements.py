from typing import *
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        
        counter = Counter(nums)

        print(counter)
        result = []
        
        
        for key in sorted(counter, key=counter.get, reverse=True):
            if(k<1):
                break
            else:
                result.append(key)
                k-=1
                
        return result 



# Runtime: 105 ms, faster than 95.26% of Python3 online submissions for Top K Frequent Elements.
# Memory Usage: 18.6 MB, less than 70.42% of Python3 online submissions for Top K Frequent Elements.
