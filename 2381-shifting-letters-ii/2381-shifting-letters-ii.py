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
            string[j] = chr((ord(s[j]) - 97 + prefix[j]) % 26 + 97)
        
        return "".join(string)
