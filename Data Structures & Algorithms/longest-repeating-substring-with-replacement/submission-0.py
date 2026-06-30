class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        seen = defaultdict(int)
        maxFreq = 0
        ans = 0
        for r in range(len(s)):
            seen[s[r]] += 1
            maxFreq = max(seen[s[r]], maxFreq)

            while (r-l+1) - maxFreq > k:
                seen[s[l]] -= 1
                l += 1
            
            ans = max(ans, r-l+1)
        return ans 