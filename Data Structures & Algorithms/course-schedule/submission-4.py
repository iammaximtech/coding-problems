class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqs = {i:[] for i in range(numCourses)}
        visited = set()

        for pre in prerequisites: 
            prereqs[pre[0]].append(pre[1])
        def dfs(i):
            if i in visited:
                return False
            if prereqs[i]==[]:
                return True
            visited.add(i)
            for pre in prereqs[i]:
                if not dfs(pre):
                    return False
            prereqs[i]=[]
            visited.remove(i)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True