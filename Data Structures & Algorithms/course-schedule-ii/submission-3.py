class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereqs = {i:[] for i in range(numCourses)}
        visited = set()
        ordered = set()
        ans = []

        for pre in prerequisites: 
            prereqs[pre[0]].append(pre[1])
        def dfs(i):
            if i in visited:
                return False
            if i in ordered:
                return True
            visited.add(i)
            for pre in prereqs[i]:
                if not dfs(pre):
                    return False
            ordered.add(i)
            ans.append(i)
            prereqs[i]=[]
            visited.remove(i)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []
        return ans