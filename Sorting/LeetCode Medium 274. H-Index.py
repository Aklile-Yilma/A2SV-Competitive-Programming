class Solution:
    def hIndex(self, citations: List[int]) -> int:

        # sprt such that to find the number of papers <= number of citations of that indexs value
        # sprt in reverse because we are searching for the maximum possible value
        citations.sort( reverse = True )

        for idx, citation in enumerate(citations):

            # find the first index where citation is smaller than or equal to array index
            if idx >= citation:
                return idx

        # since every citation is greater than the idx at citation value, we will return the whole length, because every value is valid
        return len(citations)
