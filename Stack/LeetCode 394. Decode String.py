class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for i in range(len(s)):
            if s[i] != "]":
                #appending characters
                stack.append(s[i])
            else:

                substr = ""

                while stack[-1] != "[":
                    #create substring keeping the order
                    substr = stack.pop() + substr

                # remove the opening bracket from the stack
                stack.pop()

                k = ""
                while stack and stack[-1].isdigit():
                    #create num keeping the order
                    k = stack.pop() + k

                # append substring k times
                stack.append(int(k) * substr)

        return ''.join(stack)
