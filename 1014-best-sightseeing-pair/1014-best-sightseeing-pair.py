class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        
        max_score = values[0] + 0
        ans = 0
        
        for i in range(1, len(values)):
            
            ans = max(ans, max_score + values[i] - i)
            max_score = max(max_score, values[i] + i)
        
        
        return ans