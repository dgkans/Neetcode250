class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        num1=num2 = 0
        for i, v in enumerate(tokens):
            if v == "+": 
                num2, num1=stack.pop(),stack.pop()
                stack.append(num1+num2)
            elif v == "-":
                num2, num1=stack.pop(),stack.pop()
                stack.append(num1 - num2)
            elif v == "*":
                num2, num1=stack.pop(),stack.pop()
                stack.append(int(num1 * num2))
            elif v == "/":
                num2, num1=stack.pop(),stack.pop()
                stack.append(int(num1 / num2)) 
            else:
                stack.append(int(v))
        return stack[-1]
