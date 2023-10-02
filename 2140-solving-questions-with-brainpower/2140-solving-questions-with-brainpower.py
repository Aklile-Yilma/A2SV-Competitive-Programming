class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        
        max_pt = 0
        size = len(questions)
        dp = [0] * (size)
        
        for i in range(size-1, -1, -1):
            curr_pt = questions[i][0]
            curr_skip = questions[i][1]
            dp[i] = max(max_pt, curr_pt + dp[i + curr_skip + 1] if (i + curr_skip + 1) < size else curr_pt)
            max_pt = dp[i]
            
        return max_pt
        