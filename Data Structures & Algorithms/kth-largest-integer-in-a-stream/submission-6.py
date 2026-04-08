class KthLargest:

    # use a min heap that will only ever store k items
    # popping from min heap will remove the smallest items
    # remainder is heap[0], which is the kth largest

    def __init__(self, k: int, nums: List[int]):
        self.heap = nums
        self.k = k
        heapq.heapify(self.heap)

        # pop until only k items remain
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)

        # pop to remain at k items
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)

        # 0th index is k largest
        return self.heap[0]
        
