class TimeMap:
    """
    unlike a dict, this can store multiple values for the same key, so a list.
    ex: "alice" -> ["happy", "sad"]

    then the user wants to retrieve a key's value at a timestamp, so we need to store the timestamp too.
    ex: "alice" -> [("happy", 1), ("sad", 3)]

    thankfully all calls to set() are in increasing order, so the timestamp is sorted in ascending order.
    this means we can use binary search on the get() method to find the key's value at timestamp.

    get() needs to return the most recent value of key where the prev_timestamp is <= than the timestamp param.
    this means we can't simply check the prev_timestamp == timestamp in the binary search.
    we need to find the pivot point where prev_timestamp + 1 is greater than timestamp.
    """

    def __init__(self):
        self.times = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.times[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.times:
            return ""

        values = self.times[key]

        # edge case when the last timestamp in the values list is smaller than timestamp parameter
        if values[len(values) - 1][1] <= timestamp:
            return values[len(values) - 1][0]
        
        # binary search the values list by timestamp
        left = 0
        right = len(values) - 1
        while left <= right:
            mid = (left + right) // 2
            prev_timestamp = values[mid][1]
            print(values, timestamp)
            
            if prev_timestamp == timestamp:
                # found value at exact time
                return values[mid][0]
            if prev_timestamp < timestamp and mid + 1 < len(values) and values[mid + 1][1] > timestamp:
                # found the pivot point where prev_timestamp < timestamp
                return values[mid][0]

            if prev_timestamp > timestamp:
                # prev timestamp too large, move left
                right = mid - 1
            else:
                # prev timestamp too small, move right
                left = mid + 1
        return ""
