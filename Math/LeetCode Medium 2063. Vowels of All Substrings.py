class Solution:
    def countVowels(self, word: str) -> int:
        #?
        count, size = 0, len(word)
        vowel_dict = {'a':1, 'e':1,'i':1,'o':1,'u':1}

        for idx in range(size):
                if word[idx] in vowel_dict:
                    count += (size-idx)*(idx+1)
        return count
