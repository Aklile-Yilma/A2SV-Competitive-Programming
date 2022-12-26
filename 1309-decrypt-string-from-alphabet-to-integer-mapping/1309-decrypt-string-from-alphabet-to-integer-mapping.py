class Solution:    
    def freqAlphabets(self, s: str) -> str:
        decrypted_string = []
        i = 0

        while i < len(s):
            
            # if the character at 2 indexes after the current index is pound that means it's a character from j to z
            if i + 2 < len(s) and s[i + 2] == '#':
                # split the string from i to i+2
                val = int(s[i: i + 2])
                # chr(65 - 90) is 'A' to 'Z', chr(97 - 122) is 'a' to 'z'
                decrypted_string.append(chr(val + 96)) 
                i += 3
            else:
                # for characters from a to z                 
                decrypted_string.append(chr(int(s[i]) + 96))
                i += 1

        return ''.join(decrypted_string)
