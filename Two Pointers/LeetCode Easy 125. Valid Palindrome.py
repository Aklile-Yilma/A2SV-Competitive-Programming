class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = ((s.replace(' ', '')).lower())

        # removing all non-alpha numerics
        s = ''.join(char for char in s if char.isalnum())


        left, right = 0, len(s) - 1

        while left < right:

            # find any case in which opposite letters are not the same
            if(s[left] != s[right]):
                return False

            left += 1
            right -= 1

        return True
