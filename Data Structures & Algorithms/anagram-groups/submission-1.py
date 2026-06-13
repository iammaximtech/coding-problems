class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrammap = defaultdict(list)
        for s in strs:
            sortedstr= "".join(sorted(s))
            anagrammap[sortedstr].append(s)
        return list(anagrammap.values())



        
