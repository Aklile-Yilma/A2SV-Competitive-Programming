class Solution:
    def similarPairs(self, words: List[str]) -> int:
        
        pairs = 0
        
        # use set to remove duplicates
        for idx, word in enumerate(words):
            words[idx] = set(word)
            

        for idx1 in range(len(words)):
            for idx2 in range(idx1+1, len(words), 1):
                # increase the number of pairs if they are equal
                if(words[idx1] == words[idx2]):
                    pairs += 1
                          
        return pairs
                    