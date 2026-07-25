class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        adj = collections.defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i]+"*"+word[i+1:]
                adj[pattern].append(word)
        dq= deque()
        visited = set()
        dq.append(beginWord)
        visited.add(beginWord)
        size = 1
        while dq:
            length = len(dq)
            for i in range(length):
                curr = dq.popleft()
                for j in range(len(curr)):
                    pattern = curr[:j]+"*"+curr[j+1:]
                    for word in adj[pattern]:
                        if word not in visited:
                            if word == endWord:
                                return size+1
                            dq.append(word)
                            visited.add(word)
            size += 1
        return 0

        