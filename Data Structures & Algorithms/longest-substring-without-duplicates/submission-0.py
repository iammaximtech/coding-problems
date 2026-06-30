class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        seen = {}
        l = 0
        for r in range(len(s)):
            if s[r] in seen and seen[s[r]]>=l:
                l = seen[s[r]] +1
            seen[s[r]] = r
            longest = max(longest, r-l+1)
                
        return longest 
        