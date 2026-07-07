class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        charmap = [0]* 26
        size = len(s1)
        for c in s1:
            charmap[ord(c.lower())-ord("a")] += 1
        l, r =0, 0
        seen = [0]*26
        while r<len(s2):
            seen[ord(s2[r].lower())-ord("a")] += 1
            if r-l+1 == size and seen == charmap:
                return True
            if r-l+1==size:
                seen[ord(s2[l].lower())-ord("a")] -= 1
                l += 1
            r += 1
        return False
            
            

        