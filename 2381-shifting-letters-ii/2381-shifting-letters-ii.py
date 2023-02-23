class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        prefix = [0]*(len(s)+1)

        #create prefix sum
        for start,end,direction in shifts:                
            if direction == 0:
                prefix[start] += -1
                prefix[end+1] += 1
            else:
                prefix[start] += 1
                prefix[end+1] += -1
        
        
        #compute running sum
        for i in range(1, len(prefix)):
            prefix[i] += prefix[i-1]
        
        
        string = list(s)
        for j in range(len(s)):
            # string[j] = chr(ord(s[j]) + prefix[j])
            num_ord = ord(s[j]) + (prefix[j]%26)
                        
            if num_ord > ord('z'):
                num_ord = num_ord % ord('z') + ord('a') - 1
            elif num_ord < ord('a'):
                num_ord = ord('z') + (num_ord - ord('a')) + 1
                
            string[j] = chr(num_ord)
        
        return "".join(string)
