class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # s only contains upper-case english chars
        # dict of 26 alpha chars -> freq count
        # get the char with max freq of the sliding window
        # window_len - max_freq <= k ; if false left ptr += 1
        alp_dict = defaultdict(int)
        max_len = 1

        # set initial freq
        left = 0
        right = 0
        alp_dict[s[right]] = 1

        while right < len(s):
            # find the letter with max freq - O(1) because 26 is constant
            max_freq = 0
            max_letter = "A"
            for letter, freq in alp_dict.items():
                if freq > max_freq:
                    max_freq = freq
                    max_letter = letter
            print(alp_dict)

            # for this window, can we replace k times where length is satisfied?
            cur_len = (right - left) + 1
            satisfied = cur_len - max_freq <= k
            if satisfied:
                # can replace k times! increment window size (move right ptr)
                max_len = max(max_len, cur_len)
                right += 1
                if right < len(s):
                    alp_dict[s[right]] += 1
            else:
                # cannot replace k times. decrement window size (move left ptr)
                alp_dict[s[left]] -= 1
                left += 1
        return max_len