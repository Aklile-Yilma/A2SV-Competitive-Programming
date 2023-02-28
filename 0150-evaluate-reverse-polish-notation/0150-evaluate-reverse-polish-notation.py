class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        
        for token in tokens:
            if token.lstrip('-').isdigit():
                stack.append(int(token))
            else:
                
                num2 = stack.pop()
                num1 = stack.pop()
                result = 0
                
                if token == "+":
                    result = num1 + num2
                elif token == '-':
                    result = num1 - num2
                elif token == '*':
                    result = num1 * num2
                else:
                    result = num1 / num2
                    if result > 0:
                        result = math.floor(result)
                    else:
                        result = math.ceil(result)
                
                stack.append(result)
                
        return stack[0]