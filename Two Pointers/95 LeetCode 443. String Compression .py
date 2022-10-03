
from typing import *
class Solution:
    def compress(self, chars: List[str]) -> int:

        left = 0
        right = 1

        while left < len(chars):
            count = 1

            while right < len(chars) and chars[left] == chars[right]:
                # print(chars[right])
                count += 1
                right += 1


            chars[left:right] = chars[left]
            
            if(count != 1):
                num = left
                count = f"{count}"
                if(int(count) >= 10):
                    for char in count:
                        left+=1
                        chars.insert(left, char)
                else:
                    chars.insert(left + 1, count)
                left = num + 1 + len(count) 
            else:
                left = right 
            
            right = left + 1
            
        return chars
            

s = Solution()
print(s.compress(["a","a","a","a","a","a","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","c","c","c","c","c","c","c","c","c","c","c","c","c","c"]))