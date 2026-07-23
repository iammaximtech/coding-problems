class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(l,r):
            while l>=0 and r<len(s) and s[l]==s[r]:
                l-=1
                r+=1
            return (l+1, r-1)
        ans = ""
        anslen = 0
        for i in range(len(s)):
            ##evencase 
            l,r = expand(i,i+1)
            if r-l+1>anslen:
                anslen = r-l+1
                ans = s[l:r+1]
            #oddcase
            l,r = expand(i,i)
            if r-l+1>anslen:
                anslen = r-l+1
                ans = s[l:r+1]
        return ans
            