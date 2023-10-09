class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        
        stack = []
        for char in s:
            if stack and stack[-1][0] == char and stack[-1][1] == k-1:
                stack.pop()
            else:
                if stack and stack[-1][0] == char:
                    char, count = stack.pop()
                    stack.append([char, count+1])
                else:
                    stack.append([char, 1])

        #build string
        letters = []
        while stack:
            char, count = stack.pop()
            letters.append(char* count)

        letters.reverse()

        return ''.join(letters)
