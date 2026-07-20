class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        count = {}
        ans = []
        for i in range(len(s)):
            count[s[i]] = i
        left = right = 0
        projectedEnd = 0
        while right<len(s):
            projectedEnd = max(projectedEnd, count[s[right]])
            if projectedEnd == right:
                ans.append(right-left+1)
                projectedEnd = right+1
                left = right+1
            right+=1
        return ans
