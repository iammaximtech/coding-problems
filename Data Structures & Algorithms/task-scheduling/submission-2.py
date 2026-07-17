class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = [0]*26
        for i in range(len(tasks)):
            count[ord(tasks[i])-ord("A")]+=1
        count.sort()
        maxf = count[25]
        maxCount = 0
        for i in range(26):
            if count[i] == maxf:
                maxCount+= 1
        time = (maxf-1)*(n+1)+maxCount
        return max(time, len(tasks))

        