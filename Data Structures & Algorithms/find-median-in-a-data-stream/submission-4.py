class MedianFinder:

    def __init__(self):
        self.small, self.big = [], []
        

    def addNum(self, num: int) -> None:
        if self.small and num <= -self.small[0]:
            heapq.heappush(self.small,-num)
        else:
            heapq.heappush(self.big, num)
        if len(self.small)>len(self.big)+1:
            heapq.heappush(self.big, -(heapq.heappop(self.small)))
        if len(self.big)>len(self.small)+1:
            heapq.heappush(self.small, -(heapq.heappop(self.big)))
        

    def findMedian(self) -> float:
        if len(self.small)>len(self.big):
            return -self.small[0]
        elif len(self.small)<len(self.big):
            return self.big[0]
        else:
            return (-self.small[0]+self.big[0])/2
        