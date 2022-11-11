class Solution:
    def reverseWords(self, s: str) -> str:


        # convert to list because string is immutable
        words = s.split(' ')


        for idx, word in enumerate(words):
            left = 0
            right = len(word) - 1

            # because string doesn't support item assignment: its immutable
            current_word = list(word)


            # reverse word using two-pointers approach
            while left < right:
                current_word[left], current_word[right] = current_word[right], current_word[left]

                left += 1
                right -= 1


            # convert to string and replace the original word with reversed word
            words[idx] = ''.join(current_word)

        return " ".join(words)
