class Solution:
    def pancakeSort(self, arr):
        
        """
        So the Approach is to find out maximum element the put in in 0 index and flip the array.
and Keep repeating it until the array is sorted.
        """

        end = len(arr) - 1
        Idx =  arr.index(max(arr))
        arr[:Idx+1] =  reversed(arr[:Idx+1])
        arr.reverse()
        res = [Idx+1, end+1] 
        
        while end > 0:
            Idx = arr.index(max(arr[:end]))
            arr[:Idx+1] =  reversed(arr[:Idx+1])
            arr[:end] = reversed(arr[:end])
            res.append(Idx+1)
            res.append(end)
            end -= 1
            
        return res
