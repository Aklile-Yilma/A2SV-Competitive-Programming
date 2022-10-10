
class Solution:
    def maxVowels(self, s: str, k: int) -> int:

        vowels = {'a': 1, 'e': 1, 'i':3, 'o':1, 'u':1}


        left, right = 0, 0

        result, total = 0, 0

        for right, letter in enumerate(s):

            # if letter is a vowel add to total
            if(letter in vowels.keys()):
                total += 1

            #if window is maximum move left pointer
            if((right-left) >= k):
                #if item at left pointer is vowel decreament total
                if(s[left] in vowels.keys()):
                    total -= 1

                left += 1

            result = max(result, total)

        return result
