class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        #window-size is len(cardpoints) - k

        #setting the left and right pointer
        left, right = 0 , len(cardPoints) - k

        #initial total equals to numbers outside our window
        total = sum(cardPoints[right:])
        result = total

        while right < len(cardPoints):

            #adding the left pointer value to our sum and removing the right hand side from our sum
            total += (cardPoints[left] - cardPoints[right])

            result = max(result, total)

            left += 1
            right += 1



        return result

