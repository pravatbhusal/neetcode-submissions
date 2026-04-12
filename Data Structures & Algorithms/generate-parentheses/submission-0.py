class Solution:
    """
    Keep count of open and close count of paranthesis.
    To balance paranthesis, if close < open, then we can add a close paranthesis.

    Ex: n = 3
    open = 1, close = 0 -> (
    open = 1, close = 1 -> ()
    open = 2, close = 1 -> (()
    open = 2, close = 2 -> (())
    open = 3, close = 2 -> ((())
    open = 3, close = 3 -> ((())) <- valid when open = close = n
    ...
    open = 2, close = 1 -> (()
    open = 3, close = 1 -> (()(
    open = 3, close = 2 -> (()()
    open = 3, close = 3 -> (()()) <- valid when open = close = n
    etc.
    """
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        stack = []

        def recurse(open, close):
            if open == close == n:
                # valid paranthesis
                result.append("".join(stack))
                return

            if open < n:
                # add open paranthesis
                stack.append("(")
                recurse(open + 1, close)
                stack.pop()

            if close < open:
                # add closed paranthesis
                stack.append(")")
                recurse(open, close + 1)
                stack.pop()
                
        recurse(0, 0)
        return result