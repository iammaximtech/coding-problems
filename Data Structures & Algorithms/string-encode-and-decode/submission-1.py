class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        ans = []
        for s in strs:
            ans.append(str(len(s)))
            ans.append("#")
            ans.append(s)
        return "".join(ans)

    def decode(self, s: str) -> List[str]:
        if len(s) == 0:
            return []
        ans = []
        i = 0
        while i<len(s):
            j = i
            while j<len(s) and s[j]!="#":
                j += 1
            length = int(s[i:j])
            i = j+1
            j = i+length
            ans.append(s[i:j])
            i = j
        return ans

