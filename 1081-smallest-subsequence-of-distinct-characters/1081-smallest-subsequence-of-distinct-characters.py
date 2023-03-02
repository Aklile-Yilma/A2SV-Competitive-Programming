class Solution:
    def smallestSubsequence(self, s: str) -> str:
        
        letter_count = Counter(s)
        # monotonically increasing
        stack = []
        stack_set = set()
        
        for letter in s:
            
            if letter not in stack_set:
                while stack and stack[-1] >= letter and letter_count[stack[-1]] > 0:
                    popped_letter = stack.pop()                
                    stack_set.remove(popped_letter)
                    
                stack.append(letter)
                stack_set.add(letter)
                
            #process char
            letter_count[letter] -= 1
            
            
        return ''.join(stack)
        