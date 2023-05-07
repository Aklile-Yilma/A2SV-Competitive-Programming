class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        counter = Counter(words)
        heap = []
        
        # use negative to create a max heap
        for word in counter:
            count = counter[word]
            heappush(heap, (-count, word))
            
        answer = []
        for idx in range(k):
            count, word = heappop(heap)
            answer.append(word)

        return answer