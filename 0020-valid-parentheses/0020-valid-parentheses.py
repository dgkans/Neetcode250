class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i,v in enumerate(s):
            if v == "(" or v == "{" or v == "[":
                stack.append(v)
            else:
                if stack:
                    if v == ")" and stack[-1] == "(":
                        stack.pop()
                    elif v == "}" and stack[-1] == "{":
                        stack.pop()
                    elif v == "]" and stack[-1] == "[":
                        stack.pop()
                    else:
                        return False
                else:
                    return False
        return len(stack) == 0
