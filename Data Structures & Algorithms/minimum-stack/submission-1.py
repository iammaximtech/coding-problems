class MinStack:

    def __init__(self):
         self.stack = []
         self.least = float("inf")

    def push(self, val: int) -> None:
        self.stack.append(val - self.least)
        self.least = min(val, self.least)

    def pop(self) -> None:
        pop = self.stack.pop()
        if pop < 0:
            self.least = self.least -pop

    def top(self) -> int:
        top = self.stack[-1]

        return top+self.least if top>0 else self.least

    def getMin(self) -> int:
        return self.least