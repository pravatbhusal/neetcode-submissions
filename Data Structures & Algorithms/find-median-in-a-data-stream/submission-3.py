class MedianFinder:

    def __init__(self):
        self.result = []

    def addNum(self, num: int) -> None:
        self.result.append(num)
        self.result.sort()

    def findMedian(self) -> float:
        mid = len(self.result) // 2
        if len(self.result) % 2 == 0:
            # get the median (even case)
            return (self.result[mid - 1] + self.result[mid]) / 2
        # return the median (odd)
        return self.result[mid]
        