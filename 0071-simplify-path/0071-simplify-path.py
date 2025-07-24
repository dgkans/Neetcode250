class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        tokens=path.split('/')
        for t in tokens:
            if t == '.' or t == "":
                continue
            if t == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(t)
        return '/' + '/'.join(stack)