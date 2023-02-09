class Solution:
    def compress(self, chars: List[str]) -> int:

        left = 0
        right = 1

        while left < len(chars):
            count = 1

            # move right pointer while the right value is equal to initial left value
            while right < len(chars) and chars[left] == chars[right]:
                # print(chars[right])
                count += 1
                right += 1

            #replace everything upto but not including right
            chars[left:right] = chars[left]
            
            # if count = 1 no number is inserted
            if(count != 1):
                num = left 
                count = f"{count}"
                if(int(count) >= 10):
                    for char in count:
                        num+=1
                        chars.insert(num, char)
                else:
                    chars.insert(left + 1, count)
                # move the left pointer one step and length of count because they have been inserted
                left = left + 1 + len(count)
            else:
                left = right 
            
            right = left + 1
            
            
                
 
        

