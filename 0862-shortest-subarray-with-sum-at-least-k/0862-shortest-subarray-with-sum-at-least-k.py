class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        size = len(nums)
        prefix = [0]*(len(nums) + 1)
        answer = size + 1
        
        for idx in range(len(nums)):
            prefix[idx+1] = prefix[idx] + nums[idx]
        
        q = deque()
        
        for idx in range(len(prefix)):
            
            while q and prefix[q[-1]] >= prefix[idx]:
                q.pop()
                
            while q and prefix[idx] - prefix[q[0]] >= k:
                answer = min(answer, idx - q[0])
                q.popleft()
            
            q.append(idx)
            
        return answer if answer < size+1 else -1
                