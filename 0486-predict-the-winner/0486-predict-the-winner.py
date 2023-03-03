class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        
        self.nums = nums
        def predict(left, right, score1, score2, turn):
            
            if left > right:
                return score1 >= score2
            
            if turn:
                return predict(left+1, right, self.nums[left] + score1, score2, not turn) or predict(left, right-1, self.nums[right] + score1, score2, not turn)
            else:
                return predict(left+1, right, score1, score2 + self.nums[left], not turn) and predict(left, right-1, score1, self.nums[right] + score2, not turn)
            
        return predict(0, len(self.nums)-1, 0, 0, True)
    
    
            
            
            