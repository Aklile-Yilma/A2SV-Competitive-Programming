class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        # {the end of the subsequence: [list containing lengths of different subseqeunces]}       
        end = defaultdict(list)
        
        for num in nums:
            before = num - 1
            if end[before]:
                min_len = heappop(end[before])
                heappush(end[num], min_len + 1)
            else:
                heappush(end[num], 1)
                
        #find if a subsequence is less than 3
        for value in end.values():
            for v in value:
                if v < 3:
                    return False
                
        return True
            
        
        