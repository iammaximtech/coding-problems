class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        seen = {}
        for char in s:
            seen[char] = seen.get(char,0)+1
        for char in t:
            seen[char] = seen.get(char,0)-1
            if seen[char] == 0:
                seen.pop(char)
        return not seen

        