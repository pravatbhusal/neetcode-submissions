class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # result is an array with every index is the number of days
        # example: result[0] is the number of days after the 1st day before a warmer temp appears
        # so this means we're tracking the number of days until there's a warmer temp than the current day
        # example: [30, 38, 30] -> [1, 0, 0] because 30 -> 38 is only 1 step, 38 has no warmer days, 30 is end of list
        
        # naive solution easily solved in O(N^2), so there must be an O(N) solution.
        # stacks are helpful when we need to track previous state, which this problem requires.
        # try to break the problem down to smaller pieces, like [35, 28, 38, 30]
        # iterate backwards at 30 and set to 0 (end of list), add 30 to stack
        # then go to 38 and pop prev which is 30 so set to 0, add 38 to stack
        # then go to 28 and pop prev which is 38 so set to 1, add 28 to stack
        # at 35 we only have 28 at stack so it will assume none and set to 0, which is incorrect..

        # monotonic decreasing stack problem (meaning from stack bottom to top are in decreasing order):
        # correct solution is use a stack that stores the index of the previous element
        # keep popping from stack while the current temp is greater than the item in stack
        # as we pop, update the days that it took to find the greater temperature, which equates to: cur_i - pop_i

        result = [0] * len(temperatures)
        stack = deque()

        for i, temp in enumerate(temperatures):
            # keep looping while current temp is greater than smallest item in stack
            while stack and temp > temperatures[stack[-1]]:
                # current temp is the next greater temperature for prev_i
                prev_i = stack.pop()
                days = i - prev_i
                result[prev_i] = days
            stack.append(i)

        return result