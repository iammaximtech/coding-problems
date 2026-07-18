class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        curr = []

        def backtrackdfs(i):
            if i == len(s):
                ans.append(curr.copy())
                return
            for right in range(i, len(s)):
                if self.isPalindrome(s, i, right):
                    curr.append(s[i: right+1])
                    backtrackdfs(right+1)
                    curr.pop()

        backtrackdfs(0)
        return ans
    def isPalindrome(self, s, l, r):
        if l>r:
            return False
        while l<r:
            if s[l]!=s[r]:
                return False
            l += 1
            r -= 1
        return True
        