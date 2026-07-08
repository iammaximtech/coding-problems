class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        stack = []
        for i in range(len(temps)):
            while stack and temps[stack[-1]]<temps[i]:
                ind = stack.pop()
                temps[ind] = i-ind
            stack.append(i)
        while stack:
            ind = stack.pop()
            temps[ind] = 0
        return temps
