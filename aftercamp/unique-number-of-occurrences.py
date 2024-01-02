class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        
        counter = Counter(arr)

        occurances = counter.values()

        return len(occurances) == len(set(occurances))