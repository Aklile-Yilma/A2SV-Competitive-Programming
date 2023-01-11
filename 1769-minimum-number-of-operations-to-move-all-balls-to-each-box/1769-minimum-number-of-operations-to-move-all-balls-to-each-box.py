class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        
        answer = [0] * len(boxes)
        
        for idx1, box in enumerate(boxes):
            for idx2, box2 in enumerate(boxes):
                
                if(idx1!= idx2 and box2 == "1"):
                    answer[idx1] += abs(idx1 - idx2)
                    
        return answer
                
                
        
        
        
        
        
        