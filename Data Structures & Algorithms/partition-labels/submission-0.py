class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        count = {}
        ans = []
        for i in range(len(s)):
            count[s[i]] = i
        l = 0
        maybe = 0
        start = 0
        while l<len(s):
            if count[s[l]] > l:
                maybe = max(maybe, count[s[l]])
            if count[s[l]] == maybe == l:
                ans.append(l-start+1)
                maybe = l+1
                start = l+1
            l+=1
        return ans
