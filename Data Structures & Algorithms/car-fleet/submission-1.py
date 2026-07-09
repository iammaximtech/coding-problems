class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if len(position)==0:
            return 0

        pairs = [(p,s) for p,s in zip(position, speed)]
        pairs.sort(reverse = True)
        
        lastTime = float(target-pairs[0][0])/pairs[0][1]
        fleet = 1
        for p,s in pairs:
            if float(target-p)/s > lastTime:
                lastTime = float(target-p)/s
                fleet += 1
        return fleet