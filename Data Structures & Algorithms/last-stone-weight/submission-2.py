class Solution:
    """
    stones[i] = weight of stone i

    x = largest stone
    y = 2nd largest stone
    stones[x] - stones[y] = remainder
    stones[x] = remainder

    keep smashing the stonex until there is only 0 or 1 stones remaining
    """

    """
    Solution: a max heap where heap[0] is the largest stone
    and heappop to get the 2nd largest stone

    smash the two stones, then heappush the remainder.

    keep doing this until there is only 1 or 0 items in the heap.
    """
    def lastStoneWeight(self, stones: List[int]) -> int:
        # set all stones to negative (to simulate max heap)
        max_heap = [-n for n in stones]
        heapq.heapify(max_heap)

        # keep smashing till there's only 0 or 1 stones left
        while len(max_heap) >= 2:
            largest = -heapq.heappop(max_heap)
            second_largest = -heapq.heappop(max_heap)
            remainder = largest - second_largest
            heapq.heappush(max_heap, -remainder)

        return -max_heap[0] if len(max_heap) == 1 else 0
        