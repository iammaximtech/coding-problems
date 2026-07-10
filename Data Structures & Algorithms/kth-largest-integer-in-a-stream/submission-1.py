from collections import deque
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.dq= deque(sorted(nums))
        self.k = k
        

    def add(self, val: int) -> int:
        temp = []
        while len(self.dq) > 0 and self.dq[0]<val:
            temp.append(self.dq.popleft())
        self.dq.appendleft(val)
        self.dq.extendleft(reversed(temp))
        return self.dq[-(self.k)]

