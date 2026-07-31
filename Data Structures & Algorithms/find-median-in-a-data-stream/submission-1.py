class MedianFinder:

    def __init__(self):
        self.stream = []
        self.med = 0
        

    def addNum(self, num: int) -> None:
        self.stream.append(num)
        self.stream.sort()
        n = len(self.stream)
        med = n//2
        if n%2==0:
            self.med = (self.stream[med]+self.stream[med-1])/2
        else:
            self.med = self.stream[med]
        

    def findMedian(self) -> float:
        return self.med
        
        