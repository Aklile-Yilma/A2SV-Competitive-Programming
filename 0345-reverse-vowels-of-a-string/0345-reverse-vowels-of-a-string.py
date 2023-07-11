class Solution:
    def reverseVowels(self, s: str) -> str:
        
        letters = list(s)
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        left, right = 0, len(s) - 1
        
        while left < right:
            
            if letters[left] not in vowels:
                left += 1
            
            if letters[right] not in vowels:
                right -= 1
                
            if letters[left] in vowels and letters[right] in vowels:
                letters[left], letters[right] = letters[right], letters[left]
                left += 1
                right -= 1
                
        return ''.join(letters)