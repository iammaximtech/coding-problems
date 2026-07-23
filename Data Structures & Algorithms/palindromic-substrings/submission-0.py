class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = set()
        
        def expand(l,r):
            while l>=0 and r<len(s) and s[l]==s[r]:
                ans.add((l,r))
                l-=1
                r+=1
        
        for i in range(len(s)):
            ##evencase 
            expand(i,i+1)
            #oddcase
            expand(i,i)
        return len(ans)
        