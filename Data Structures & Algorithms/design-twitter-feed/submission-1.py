class Twitter:

    def __init__(self):
        self.KfollowsV_graph = defaultdict(set)
        self.tweet_order = []
        # self.user2tweets = defaultdict(list)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        # self.user2tweets[userId].append(tweetId)
        self.tweet_order.append((userId, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        visible_users = self.KfollowsV_graph[userId] | {userId}
        res = []
        for uid, tid in reversed(self.tweet_order):
            if uid in visible_users:
                res.append(tid)
                if len(res) == 10: break
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.KfollowsV_graph[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.KfollowsV_graph[followerId].discard(followeeId)
