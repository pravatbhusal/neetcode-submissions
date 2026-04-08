class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return self.naive(nums, k)

    # naive solution is to store a dict of frequencies
    # then sort the dict by frequencies O(NLog(N))
    """
    key -> freq
    1 -> 1
    2 -> 2
    3 -> 3
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
