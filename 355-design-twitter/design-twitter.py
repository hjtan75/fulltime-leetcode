class Twitter:

    def __init__(self):
        self.followDict = {} # followerId, set(followeeid)
        self.followedByDict = {} # followeeId, set(followerId)
        self.postByAUser = {} # userid, list(postId)
        self.time = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.postByAUser:
            self.postByAUser[userId] = []
        self.postByAUser[userId].append((-self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        newsFeed = []
        if userId in self.postByAUser:
            newsFeed += self.postByAUser[userId]

        for followeeId in self.followDict.get(userId, []):
            if followeeId in self.postByAUser:
                newsFeed += self.postByAUser[followeeId]

        heapq.heapify(newsFeed)
        timed_news_feed = heapq.nsmallest(10, newsFeed)
        res = []

        for time, postId in timed_news_feed:
            res.append(postId)
        
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followDict:
            self.followDict[followerId] = set()
        self.followDict[followerId].add(followeeId)

        if followeeId not in self.followedByDict:
            self.followedByDict[followeeId] = set()
        self.followedByDict[followeeId].add(followerId)
    
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followDict:
            self.followDict[followerId].remove(followeeId)

        if followeeId in self.followedByDict:
            self.followedByDict[followeeId].remove(followerId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)