"""
Valid Paranthesis problem was solved using a stack. Push open paranthesis and
pop when encountering close paranthesis then verify open and close match.

The catch with this problem "*" has 3 decisions: empty, open, or closed.

Greedy Solution (WRONG intuition):
This problem can be solved by counting the number of open paranthesis,
number of close paranthesis, and number of *. Then greedily picking which
is the best to use for *.

Local optima (greedy): Keep balancing the number of paranthesis while iterating.
1. If there are a lot of open paranthesis in the stack and not enough closing, use closed.
2. If there are not enough open paranthesis in the stack but lots of closing, use open.
3. If count is currently balanced, use empty string.

Note: This is WRONG intuition because we're committing to a decision for "*".
See where in this example "*(" it would break.

Stack Solution (O(N) space):
Instead of committing to one use of *, track the range of possible balances.

Push both open paran and "*" chars to the stack and when we encounter a closing
paran and we pop from the stack see a "*" we treat it as a open paran.

If at the end stack is not empty, we match remaining open paran with "*" as
closing paran to balance. Any remaining stars are treated as empty string.
To ensure the remaining open parans have a closing paran after it, we must
track the indices.

Greedy Solution (Correct):
Unlike Valid Parentheses which requires O(N) space due to multiple bracket
types, this problem only has '(' and ')' so a counter range suffices.

Count the number of open paranthesis and decrement when we encounter a closing
paranthesis. If the number of open paranthesis ever goes below 0, return False.

For this particular problem, we need the range of min and max open parans.
If we see a "*", decrement min open paran and increment max open paran.
If max open paran goes below 0, then return False cannot balance.
If min open paran goes below 0, reset to 0 to treat "*" as empty string.
"""
class Solution:
    def checkValidString(self, s: str) -> bool:
        min_open = 0
        max_open = 0

        for paran in s:
            if paran == "(":
                min_open, max_open = min_open + 1, max_open + 1
            elif paran == ")":
                min_open, max_open = min_open - 1, max_open - 1
            else:
                # expand range of open paranthesis
                min_open, max_open = min_open - 1, max_open + 1
            if max_open < 0:
                # too many closing parans and not enough "*", cannot balance
                return False
            if min_open < 0:
                # too many "*", set them to empty
                min_open = 0
        
        return min_open == 0