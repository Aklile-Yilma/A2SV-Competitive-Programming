

class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        # form our list of powers of 2
        pows = [2 ** i for i in range(0,22)] 
        # dict to store what we've seen - dynamic programming solution for time requirement
        dp_seen = {} 
        count = 0 # to store the answer

        for idx1 in range(0, len(deliciousness)):
            for idx2 in range(0, len(pows)):
                
                # "if we find a previous deliciousness[j] as pows[i] - deliciousness[j], then we will add dp_seen[deliciousness[j]] to count"
                if pows[idx2] - deliciousness[idx1] in dp_seen: 
                    count += dp_seen[pows[idx2] - deliciousness[idx1]]
            
            if deliciousness[idx1] in dp_seen:
                dp_seen[deliciousness[idx1]] += 1 
            else:
                dp_seen[deliciousness[idx1]] = 1
                
        return count % (10**9 + 7) # the arbitrary modulo, presumably to reduce the answer size
            
        
# class Solution:
#     def countPairs(self, deliciousness: List[int]) -> int:
        
        
#         # deliciousness.sort()
#         counter = Counter(deliciousness)
        
#         unique = list(counter.keys())
#         size = len(unique)
      
#         result = 0
#         # pairs = []
        
        
#         for idx in range(size):
#             for idx2 in range(idx+1, size, 1):
                
#                 summation = unique[idx] + unique[idx2]
                
#                 if(math.log(summation, 2).is_integer()):
#                     # pairs.append([unique[idx], unique[idx2]])
#                     result += (counter[unique[idx]] * counter[unique[idx2]])
                    
            
#         for num in unique:
#             if(counter[num] > 1):
#                 summation = num + num
                
        
#                 if(summation == 0 or math.log(summation, 2).is_integer()):
#                     result += ((counter[num]) * ((counter[num]) -1)//2)

            
#         return result % 10 ** 9 + 7
