class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        
        positive = []
        negative = []
        answer = []
        
        for num in nums:
            if(num >= 0):
                positive.append(num)
            else:
                negative.append(num)        
        
        for pos, neg in zip(positive, negative):
            answer.append(pos)
            answer.append(neg)
            
        return answer
            