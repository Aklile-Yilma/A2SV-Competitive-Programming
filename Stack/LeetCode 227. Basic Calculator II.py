class Solution:
    def calculate(self, s: str) -> int:

        # start with operator set to + because we want to append the first number to our stack before setting our actual operator
        stack, curr_num, operator = [], "" , "+"
        all_operators = {"+", "-", "*", "/"}

        for idx,char in enumerate(s):

            if char.isdigit():
                #to create to digit numbers as 1+0 in string = 10
                curr_num += char

            if char in all_operators or idx == len(s) - 1:
                # append to stack if operator is + or -
                curr_num = int(curr_num)
                if operator == "+":
                    stack.append(curr_num)
                elif operator == "-":
                    stack.append(-curr_num)
                # calculate right away only if * or /
                elif operator == "*":
                    stack[-1] *= curr_num
                elif operator == "/":
                    stack[-1] /= curr_num
                    stack[-1] = int(stack[-1])

                curr_num = ""
                operator = char

        return sum(stack)


    # WITHOUT CONSIDERING BODMAS

#         str1 = s.replace(" ", "")
#         stack = []
#         for item in s:
#             if item == " ":
#                 continue

#             if len(stack) <= 2:
#                 stack.append(item)

#             else:
#                 num2 = int(item)
#                 operation = stack.pop()
#                 num1 = int(stack.pop())


#                 if(operation == "+"):
#                     result = num1 + num2
#                 elif(operation == "-"):
#                     result = num1 - num2
#                 elif(operation == "/"):
#                     result = num1 / num2
#                 else:
#                     result = num1 * num2

#                 stack.append(result)

#         return stack[-1]

