class Solution:
    def maxProduct(self, words: List[str]) -> int:
        
        words_bits = []
        for word in words:
            curr_bit = 0
            for letter in word:
                idx = ord(letter) - 97
                curr_bit = curr_bit | (1 << idx)
            words_bits.append(curr_bit)
                
        res = 0
        for first in range(len(words)):
            word1 = words[first]
            for second in range(first+1, len(words)):
                word2 = words[second]
                
                if not (words_bits[first] & words_bits[second]):
                    res = max(res, len(word1) * len(word2))

        return res