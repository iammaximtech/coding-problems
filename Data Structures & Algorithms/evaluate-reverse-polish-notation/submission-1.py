class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for s in tokens:
            if s.isdigit():
                stack.append(int(s))
            elif s[1:].isdigit():
                stack.append(-int(s[1:]))
            else:
                op2 = stack.pop()
                op1 = stack.pop()
                if s == "+":
                    stack.append(op1+op2)
                elif s == "-":
                    stack.append(op1-op2)
                elif s == "*":
                    stack.append(op1*op2)
                else:
                    stack.append(int(op1/op2))
        return stack.pop() if stack else 0