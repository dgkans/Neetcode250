import collections
import heapq
from typing import List

class Twitter:

    def __init__(self):
        self.tweet_counter = 0
        self.tweetMap = collections.defaultdict(list)   # userId -> list of (timestamp, tweetId)
        self.followMap = collections.defaultdict(set)   # userId -> set of followeeIds

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet_counter += 1
        self.tweetMap[userId].append((self.tweet_counter, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        # Build set of users to check: followees + self
        users_to_check = set(self.followMap[userId])
        users_to_check.add(userId)
        
        # Gather all tweets from those users
        all_tweets = []
        for uid in users_to_check:
            for tweet in self.tweetMap[uid]:
                all_tweets.append(tweet)
        
        # Get 10 most recent by timestamp
        top_10 = heapq.nlargest(10, all_tweets)
        
        # Extract just the tweet IDs
        result = []
        for timestamp, tweetId in top_10:
            result.append(tweetId)
        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].discard(followeeId)