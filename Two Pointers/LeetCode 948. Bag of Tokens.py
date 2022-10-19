from typing import *
class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:

        #sort the tokens so we can move our right and left pointer accordingly to the power given
        tokens.sort()


        left, right , score = 0, len(tokens)-1, 0
        max_score = 0

        while left <= right:
            # flip token at left pointer if it is less than or equal to power
            if(tokens[left] <= power):
                score += 1
                power -= tokens[left]
                left += 1
            # play token at right pointer face down
            elif(score > 0):
                score -= 1
                power += tokens[right]
                right -= 1
            else:
                # return zero if the tokens are greater than the power given
                return 0


            max_score = max(max_score, score)


        return max_score
    
    
s = Solution()
s.bagOfTokensScore([100,200,300,400], 200)

