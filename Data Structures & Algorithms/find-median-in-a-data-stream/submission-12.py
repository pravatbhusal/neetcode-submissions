"""
Naive Solution O(N): maintaining a sorted list
- addNum insert element in sorted list where num maintains sorted order
- findMedian would return the middle index of the sorted list

Optimal Solution O(log(N)): using two heaps: min and max heap.
- max heap stores the smaller left half of the elements
- max heap's top = largest of smaller half = left mid
- min heap stores the larger right half of the elements
- min heap's top = smallest of larger half = right mid
We need to balance that each heaps has roughly an equal half of elements.
Balance rule: the two heap lengths cannot differ greater than 1

Example of balancing:

max_heap (left): [1, 2, 3]   ← size 3
min_heap (right): [4, 5]     ← size 2

If we call addNum(0), 0 is on left half, so max_heap would have size 4 and min_heap size 2 (inbalanced).
To balance, we pop out 3 from max_heap and put in min_heap, then add 0 to max_heap.
"""
class MedianFinder:

    def __init__(self):
        self.min_heap = []
        self.max_heap = []

    def addNum(self, num: int) -> None:
        if not self.min_heap:
            self.min_heap.append(num)
        elif num <= self.min_heap[0]:
            # max heap maintains smaller right half 
            heapq.heappush(self.max_heap, -num)
        else:
            # min heap maintains larger left half
            heapq.heappush(self.min_heap, num)

        # balance heaps
        size_diff = abs(len(self.min_heap) - len(self.max_heap))
        if size_diff > 1:
            if len(self.min_heap) > len(self.max_heap):
                # min heap has too many elements, pop and push to max heap
                val = heapq.heappop(self.min_heap)
                heapq.heappush(self.max_heap, -val)
            else:
                # max heap has too many elements, pop and push to min heap
                val = -heapq.heappop(self.max_heap)
                heapq.heappush(self.min_heap, val)

    def findMedian(self) -> float:
        size = len(self.min_heap) + len(self.max_heap)
        if size % 2 == 0:
            # even case
            return (self.min_heap[0] + -self.max_heap[0]) / 2
        # odd case - return from the heap with 1 extra element
        return self.min_heap[0] if len(self.min_heap) > len(self.max_heap) else -self.max_heap[0]
        