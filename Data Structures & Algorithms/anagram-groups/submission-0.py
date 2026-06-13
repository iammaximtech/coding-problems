class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrammap = {}
        for s in strs:
            sortedstr= "".join(sorted(s))
            if sortedstr not in anagrammap:
                anagrammap[sortedstr] = []
            anagrammap[sortedstr].append(s)
        return list(anagrammap.values())



        
