class Solution:

    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:

        prefix = [0]

        for i in arr:
            prefix.append(prefix[-1]^i)


        answer = []
        for query in queries:
            left = query[0]
            right = query[1]
            result = (prefix[right+1] ^ prefix[left])
            answer.append(result)

        return answer
