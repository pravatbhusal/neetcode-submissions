class Twitter:
    """
    My initial idea (INCORRECT, not efficient):

    Have a global timer that increments on each call to postTweet().

    getNewsFeed() can be solved using max heap to get top 10 posts.
    Each user has their own max heap of posts.

    On postTweet(), add the post to the user's heap and the followers heaps.

    On follow(), add all the posts of that person to the user's heap.

    On unfollow(), remove all the posts of that person from the user's heap.
    """

    """
    Correct Solution:

    follow() will add to a dictionary of userId -> set of following ids
    
    unfollow() will remove from userId's set of following ids

    Have a global timer that increments on each call to postTweet().

    Create a dictionary of userId -> list of tweets
    The last tweet in the list will be the most recent tweet

    getNewsFeed() will get all of the list of tweets of the userId and the users
    that it follows. It will add the 10 most recent items from end of those lists,
    then heapify that list (max heap). Then it will pop the 10 most recent tweets.

    How to get the 10 most recent items from the end of the lists?
    We can initially get the followee's most recent posts at the end.
    Then keep iterating backwards from each followee's list.
    """

    def __init__(self):
        self.time = 0
        self.following = defaultdict(set)
        self.tweets = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        post = (-self.time, tweetId) # negate time (max heap)
        self.tweets[userId].append(post)
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        result = []
        max_heap = []

        # add user itself as a follower
        self.following[userId].add(userId)

        # add the recent posts from user and each person the user is following
        # this only appends from the end of the each list
        for followeeId in self.following[userId]:
            if followeeId in self.tweets:
                recent_i = len(self.tweets[followeeId]) - 1
                recent_post = self.tweets[followeeId][recent_i]
                time, tweetId = recent_post

                # add the most recent post and keep track of the index
                # keeping track of the index lets us come back and check
                # the previous posts of that followee when we pop from the heap
                post = (time, tweetId, followeeId, recent_i)
                max_heap.append(post)

        # heapify the recent posts
        heapq.heapify(max_heap)

        # now get the top 10 recent posts
        while max_heap and len(result) < 10:
            recent_post = heapq.heappop(max_heap)
            time, tweetId, followeeId, recent_i = recent_post
            result.append(tweetId)

            # add the previous recent index's post to the heap
            # this greedily only gets the followee's most recent post
            if recent_i >= 1:
                prev_recent_i = recent_i - 1
                prev_recent_post = self.tweets[followeeId][prev_recent_i]
                time, tweetId = prev_recent_post
                post = (time, tweetId, followeeId, prev_recent_i)
                heapq.heappush(max_heap, post)

        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
