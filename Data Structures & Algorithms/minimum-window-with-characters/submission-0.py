from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ans = ""
        if len(s) < len(t):
            return ans

        countT = defaultdict(int)
        window = defaultdict(int)
        
        for c in t:
            countT[c] += 1
        
        need, have = len(countT), 0
        left, right = -1, -1
        minLen = len(s)+1

        l=0
        for r in range(len(s)):
            window[s[r]] += 1
            if countT[s[r]] == window[s[r]]:
                have += 1
            
            while have == need:
                if r-l+1 <minLen:
                    left, right = l, r
                    minLen = r-l+1
                window[s[l]] -= 1
                if window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        if left != -1 and right != -1:
            ans = s[left: right+1]
        return ans
        


        