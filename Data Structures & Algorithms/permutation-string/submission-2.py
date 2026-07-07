class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        s1Count, s2Count = [0]*26, [0]*26
        matches = 0

        for i in range(len(s1)):
            s1Count[ord(s1[i].lower())-ord("a")] += 1
            s2Count[ord(s2[i].lower())-ord("a")] += 1

        for i in range(26):
            if s1Count[i] == s2Count[i]:
                matches += 1

        l = 0

        for i in range(len(s1), len(s2), 1):
            if matches == 26:
                return True

            ind = ord(s2[i].lower())-ord("a")
            s2Count[ind] += 1

            if s2Count[ind] == s1Count[ind]:
                matches += 1
            if s2Count[ind] == s1Count[ind]+1:
                matches -=1

            ind = ord(s2[l].lower())-ord("a")
            s2Count[ind] -= 1
            if s2Count[ind] == s1Count[ind]:
                matches += 1
            if s2Count[ind] == s1Count[ind]-1:
                matches -=1
            l += 1

        return matches == 26


            
