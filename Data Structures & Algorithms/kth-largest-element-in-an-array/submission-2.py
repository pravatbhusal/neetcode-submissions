class Solution:
    """
    Similar problem: Kth Largest Element in a Stream

    Solution 1: Min heap of size k, time is O(N*Log(K)) space is O(K)
    Push elements and pop from heap to maintain size k.

    Solution 2: Quickselect (similar to Quicksort), time is O(N) average.
    Pick a pivot, swap elements where all elements to the left
    are less than pivot and to the right are greater than pivot.
    Divide subarray recursively till we find pivot that has k
    elements greater, meaning pivot is the kth largest element.
    Time complexity = N + N / 2 + N / 4 + N / 8 ... = 2N = O(N)
    """
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # k index in sorted array
        k_index = len(nums) - k

        def quickSelect(l, r):
            pivot, partition = nums[r], l  # set pivot to end of list (r)
            for i in range(l, r):
                if nums[i] <= pivot:
                    # nums[i] less than pivot, swap to the left partition
                    nums[partition], nums[i] = nums[i], nums[partition]
                    partition += 1
            # swap pivot between the left and right partition
            nums[partition], nums[r] = nums[r], nums[partition]

            # found pivot as the kth largest element
            if partition == k_index: return nums[partition]

            # pivot is too small, recurse the right subarray
            if partition < k_index: return quickSelect(partition + 1, r)

            # pivot is too large, recurse the left subarray
            if partition > k_index: return quickSelect(l, partition - 1)

        return quickSelect(0, len(nums) - 1)