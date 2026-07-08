from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opposites = { ")" : "(", "]" : "[", "}" : "{" }
        
        for c in s:
            if c in opposites:
                if stack and opposites[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return len(stack) == 0
        