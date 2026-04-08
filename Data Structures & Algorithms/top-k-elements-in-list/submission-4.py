class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return self.bucket_sort(nums, k)

    # bucket sort: frequency (index) -> list of numbers (bucket)
    # time = O(N), space = O(N)
    def bucket_sort(self, nums, k):
        # count frequencies (O(N))
        freqs = defaultdict(int)
        for num in nums:
            freqs[num] = freqs[num] + 1

        # initialize buckets, max freqs possible is size of nums list
        buckets = [[] for i in range(len(nums) + 1)]

        # put frequency as an index for each bucket O(N)
        for num, freq in freqs.items():
            buckets[freq].append(num)

        # reverse iterate from the buckets until top K O(N)
        k_top = []
        for freq in range(len(buckets) - 1, 0, -1):
            for num in buckets[freq]:
                k_top.append(num)
                if len(k_top) == k:
                    # done k_top, short-circuit
                    return k_top
        return k_top

    # naive solution is to store a dict of frequencies
    # then sort the dict by frequencies
    # time = O(Nlog(N)) + O(K)
    # space = O(N) + O(K)
    """
    key -> freq
    1 -> 3
    2 -> 2
    3 -> 1
    """
    def naive(self, nums, k):
        # count frequencies
        freqs = defaultdict(int)
        for num in nums:
            freqs[num] = freqs[num] + 1

        # sort dict by descending frequencies using comparator O(N(log(N)))
        desc_freqs = sorted(freqs.items(), key=lambda freq: freq[1], reverse=True)

        # get the k items O(K)
        k_freqs = desc_freqs[:k]
        return [k_freq[0] for k_freq in k_freqs]
