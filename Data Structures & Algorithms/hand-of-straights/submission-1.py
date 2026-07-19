class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize != 0:
            return False
        freq = Counter(hand)
        for num in hand:
            start = num
            while start-1 in freq:
                start -= 1
            while start<=num:
                while freq[start]:
                    for i in range(start, start+groupSize):
                        if not freq[i]:
                            return False
                        freq[i]-=1
                start += 1
            
        return True