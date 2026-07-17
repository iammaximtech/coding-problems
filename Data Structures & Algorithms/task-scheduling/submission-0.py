class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = [0]*26
        for i in range(len(tasks)):
            count[ord(tasks[i])-ord("A")]+=1
        count.sort()
        maxf = count[25]
        gaps = (maxf-1)*n
        for i in range(24,-1,-1):
            gaps -= min(maxf-1, count[i])

        return max(0, gaps)+len(tasks)