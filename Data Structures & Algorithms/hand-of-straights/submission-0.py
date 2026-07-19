class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize !=0:
            return False
        freq = {}
        for n in hand:
            freq[n] = freq.get(n, 0) + 1
        heap = list(freq.keys())
        heapq.heapify(heap)

        while heap:
            first = heap[0]
            for i in range(first, first+groupSize):
                if i not in freq:
                    return False
                freq[i]-=1
                if freq[i] == 0:
                    if i != heap[0]:
                        return False
                    heapq.heappop(heap)
        return True