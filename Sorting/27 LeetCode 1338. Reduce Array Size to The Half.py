class Solution:
    def minSetSize(self, arr: List[int]) -> int:

        counter = Counter(arr)
        values = list(counter.values())
        values.sort(reverse = True)

        sum = 0

        for i in range(len(values)):
            sum+=values[i]
            if(sum >= len(arr)/2):
                return i+1
