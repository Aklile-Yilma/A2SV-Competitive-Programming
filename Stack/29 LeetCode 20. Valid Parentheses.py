
class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        dictionary = { '(': ')', '[': ']', '{': '}'}

        for b in s:
            if b in dictionary.keys():
                # if b is open bracket add to stack
                stack.append(b)

            elif stack and  b == dictionary[stack[-1]]:
                # if b is closing of last open bracket remove last open bracket
                stack.pop(-1)

            else:
                # if b is closing bracket and no open brackets
                return False

        # if there are brackets left to close returns False
        return len(stack) == 0
