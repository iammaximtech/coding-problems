from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        dq = deque()
        opposites = defaultdict(str)
        opposites["("]=")"
        opposites["{"]="}"
        opposites["["]="]"
        
        for c in s:
            if dq and opposites[dq[0]] == c:
                dq.popleft()
            else:
                dq.appendleft(c)
        return len(dq) == 0
        