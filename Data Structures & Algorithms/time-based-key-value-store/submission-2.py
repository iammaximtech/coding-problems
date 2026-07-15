
class TimeMap:

    def __init__(self):
        self.keymap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keymap:
            self.keymap[key] = []
        self.keymap[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        timeval = self.keymap.get(key,[])
        if len(timeval)==0: return ""
        ans = ""
        n = len(timeval)
        l, r = 0, n-1
        while l<=r:
            m = l + (r-l)//2
            if timeval[m][0] <= timestamp:
                ans = timeval[m][1]
                l = m + 1
            else:
                r = m -1
        return ans
