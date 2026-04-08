class KthLargest:

    # max heap, popping gives you the kth largest element, then heapify
    # heapq is a min heap, so invert the heap to make it a max heap
    # OR more efficient is min heap, and only store k items
    def __init__(self, k: int, nums: List[int]):
        self.heap = nums
        self.k = k
        heapq.heapify(self.heap)

        # only store k largest items in min heap by popping the smaller values
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)

        # pop once to be back at k items
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)

        # 0th item in min heap of k is the kth largest of nums
        return self.heap[0]
        
