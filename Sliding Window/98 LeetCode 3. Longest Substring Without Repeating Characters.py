class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        chars = set()
        result = 0
        left = 0


        # right pointer that moves as we iterate though our list
        for right in range(len(s)):

            # while the new item will ne a duplicate in you set remove the items before it
            while s[right] in chars:
                # remove the items of s in chars
                chars.remove(s[left])
                left +=1

            # add new item to character set
            chars.add(s[right])
            result = max(result , right - left + 1)

        return result


