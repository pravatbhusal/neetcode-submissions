class MedianFinder:

    def __init__(self):
        self.result = []

    def addNum(self, num: int) -> None:
        if not self.result:
            self.result.append(num)
            return

        low = 0
        high = len(self.result) - 1

        while low <= high:
            mid = (low + high) // 2
            if self.result[mid] < num:
                # index is too small
                low = mid + 1
            else:
                # index is too large
                high = mid - 1

        # low is the correct index to insert
        self.result.insert(low, num)

    def findMedian(self) -> float:
        mid = len(self.result) // 2
        if len(self.result) % 2 == 0:
            # get the median (even case)
            return (self.result[mid - 1] + self.result[mid]) / 2
        # return the median (odd)
        return self.result[mid]
        