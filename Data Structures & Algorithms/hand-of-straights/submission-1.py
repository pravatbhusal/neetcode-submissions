"""
hand[i] = person i's hand
groupSize = number of people in group

Re-arrange the cards into groups of groupSize
The card values must be increasing by 1.

Sort solution: Sort the numbers and then break them into group sizes.
Store the numbers in a Counter (freq dict) and use that to separate the group.

Heap solution: Put all the hands in a min heap and pop to get the smallest hand.
Use a Counter to separate each same hand into a separate group.
Once a group is of groupSize, start again and create a new group.
"""
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            # short-circuit, not even group size
            return False

        freqs = Counter(hand)
        # heapify the unique values from the dict
        min_h = list(freqs.keys())
        heapq.heapify(min_h)

        while min_h:
            # start a group at first
            first = min_h[0]
            freqs[first] -= 1
            if freqs[first] == 0:
                # used up, remove from heap
                heapq.heappop(min_h)

            # verify increasing groupSize is satisfied
            for i in range(1, groupSize):
                next = first + i
                if freqs[next] == 0:
                    # gap exists, group is non-increasing
                    return False
                freqs[next] -= 1
                if freqs[next] == 0:
                    # used up, remove from heap
                    heapq.heappop(min_h)

        return True