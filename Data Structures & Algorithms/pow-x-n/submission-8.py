"""
Power of x^n is multiplying x up till n number of times. This is an O(N) solution.
Example: x = 2, n = 5 -> 2 * 2 * 2 * 2 * 2 * 2 = 64

If you notice, there's repeated work where we multiply 2 * 2 we know the result so we don't need to keep
multiplying that by the next sequence. We can solve this in O(log(N)) with divide-and-conquer.
See example 2^6 = 2^3 * 2^3, so if we have the answer to 2^3 we don't need to repeat that work twice.

This idea is called "fast exponentiation" (or exponentiation by squaring). Here's an example of fast exponentation,
which uses formula "x^n = (x^2)^(n/2)" when n is an even number:

Ex: 2^4 = (2^2)^(4/2) = 4^2 = = 16 <- Notice that we only needed 2^2 for this case
    2^2 = (2^2)^(2/2) = 4^1 = 4 <- Notice that we only needed 2^1 for this case
    2^1 = 2

We did not have to calculate 2^3 because fast exponentation skipped that calculation. Fast exponentation skips
calculating odd powers entirely, which makes this solution O(log(N)).

When n is a negative number, use the same calculation and the result we can simply return: 1 / result.
"""
class Solution:
    """
    This is a bottom-up iterative solution using binary exponentiation.
    Binary exponentiation is the inverse of the fast exponentiation formula.
    We are building the solution bottom-up, starting from result = 1 to the top result = x^n.
    """
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0

        abs_n = abs(n)
        result = 1
        while abs_n > 0:
            if abs_n % 2 == 1:
                # handle odd
                result = result * x
            # binary exponentiation
            x = x * x
            abs_n = abs_n // 2

        return result if n > 0 else 1 / result

    """
    This is a top-down recursive solution using fast exponentiation formula: x^n = (x^2)^(n/2).
    We are building the solution top-down, starting from x^n to the bottom result = 1.
    """
    def myPow_TopDown_Recursive(self, x: float, n: int) -> float:
        if x == 0:
            return 0

        def helper(x, n):
            if n == 0:
                return 1
            if n % 2 == 0:
                # handle even (fast exponentation)
                return helper(x * x, n // 2)
            else:
                # handle odd
                return x * helper(x, n - 1)

        result = helper(x, abs(n))
        return result if n > 0 else 1 / result