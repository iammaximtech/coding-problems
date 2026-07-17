class Twitter:

    def __init__(self):
        self.tweets = collections.defaultdict(collections.deque)
        self.follower = collections.defaultdict(set)
        self.time = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.follower[userId].add(userId)
        self.tweets[userId].append((self.time, tweetId))
        self.time -= 1
        if len(self.tweets[userId]) == 11:
            self.tweets[userId].popleft()
        

    def getNewsFeed(self, userId: int) -> List[int]:
        minheap = []
        for user in self.follower[userId]:
            for tweet in self.tweets[user]:
                heapq.heappush(minheap, tweet)
        ans = []
        while len(ans)<10 and minheap:
            ans.append(heapq.heappop(minheap)[1])
        return ans

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follower[followerId].add(followeeId)
        self.follower[followerId].add(followerId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.follower[followerId].discard(followeeId)
