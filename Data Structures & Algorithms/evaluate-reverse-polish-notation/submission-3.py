class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for s in tokens:
            if s == "+":
                op2, op1 = stack.pop(), stack.pop()
                stack.append(op1+op2)
            elif s == "-":
                op2, op1 = stack.pop(), stack.pop()
                stack.append(op1-op2)
            elif s == "*":
                op2, op1 = stack.pop(), stack.pop()
                stack.append(op1*op2)
            elif s == "/":
                op2, op1 = stack.pop(), stack.pop()
                stack.append(int(op1/op2))
            else:
                stack.append(int(s))
        return stack.pop() if stack else 0