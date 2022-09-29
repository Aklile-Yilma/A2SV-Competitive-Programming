class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        minQueue = deque()
        maxQueue = deque()
        
        ans = 0
        l = 0
        for r in range(len(nums)):
            # removing max elements on the left
            while maxQueue and nums[maxQueue[-1]] < nums[r]:
                maxQueue.pop()
                
            maxQueue.append(r)
            
            # removing min elements on the left
            while minQueue and nums[minQueue[-1]] > nums[r]:
                minQueue.pop()
                
            minQueue.append(r)
            
            maxEl = nums[maxQueue[0]]
            minEl = nums[minQueue[0]]
            
            if abs(maxEl - minEl) <= limit:
                ans = max(ans, r-l+1)
            else:
                # shrink window
                if l == maxQueue[0]:
                    maxQueue.popleft()
                if l == minQueue[0]:
                    minQueue.popleft()
                    
                l += 1
        return ans 





















# Time complexity issue but great first try



#  from typing import *
# import queue
# class Solution:

#     def longestSubarray(self, nums: List[int], limit: int) -> int:
        
#         result = -1
#         q= queue.deque()
        
        
#         right, left = 0, 0

#         while left < len(nums):
#             q = []
        
#             while right < len(nums):
#                 q.append(nums[right])

#                 if len(q) == 1:
#                     max_no = q[0]
#                     min_no = q[0]
#                 else:
#                     if q[-1] > max_no:
#                         max_no = q[-1]
#                     if q[-1] < min_no:
#                         min_no = q[-1]

#                 if max_no - min_no <= limit:
#                     if not result:
#                         result = len(q)
#                     elif len(q) > result:
#                         result = len(q) 
#                 else:
#                     break

#                 right+=1

#             left+=1
#             right= left
                    

#         return result


                    
s = Solution()
print(s.longestSubarray([8,2,4,7], 4))