class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c:set() for word in words for c in word}
        ans = []
        visited =set()

        for i in range(len(words)-1):
            w1 = words[i]
            w2 = words[i+1]
            minlen = min(len(w1),len(w2))
            if len(w1)>len(w2) and w1[:minlen]==w2[:minlen]:
                return ""
            for j in range(minlen):
                if w1[j]!=w2[j]:
                    adj[w1[j]].add(w2[j])
                    break
        
        def dfsTopo(c, path):
            if c in visited:
                if c in path:
                    return False
                else:
                    return True
            visited.add(c)
            path.add(c)
            for n in adj[c]:
                if not dfsTopo(n,path):
                    return False
            ans.append(c)
            path.remove(c)
            return True
        
        for k in adj:
            if k not in visited:
                if not dfsTopo(k,set()):
                    return ""
        ans.reverse()
        return "".join(ans)