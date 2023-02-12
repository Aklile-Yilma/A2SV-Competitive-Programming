class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        seats = blocks

        left, total, result = 0, 0, float('inf')

        for right, char in enumerate(seats):

            if(char == 'W'):
                total += 1


            if(right - left + 1 == k ):
                result = min(result, total)
                if(seats[left] == 'W'):
                    total -= 1
                left += 1

        return result