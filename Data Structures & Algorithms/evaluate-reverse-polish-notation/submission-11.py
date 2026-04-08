class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # similar solution as evalRPN_my_solution
        # but now i understand Reverse Polish Notation (postfix notation)
        # on operand we pop last 2 numbers, total becomes 0th index of stack
        # there will always be x numbers and x - 1 operands
        
        num_stack = deque()
        for char in tokens:
            # pop last 2 if char is operand
            if char == "+":
                num1 = num_stack.pop()
                total = num_stack.pop()
                num_stack.append(total + num1)
            elif char == "-":
                num1 = num_stack.pop()
                total = num_stack.pop()
                num_stack.append(total - num1)
            elif char == "*":
                num1 = num_stack.pop()
                total = num_stack.pop()
                num_stack.append(total * num1)
            elif char == "/":
                num1 = num_stack.pop()
                total = num_stack.pop()
                num_stack.append(int(total / num1))
            else:
                num_stack.append(int(char))
        # last item is the total sum
        # guaranteed to have 0th index since problem is always valid postfix
        return num_stack[0]

    # Below is my solution, which was very close.
    # I just didn't understand Reverse Polish notation.
    def evalRPN_my_solution(self, tokens: List[str]) -> int:
        # map operator to function call
        # keep updating result as you read next token
        # pop next token in a stack (deque) for O(1) with stack.popleft()

        # get the operands that occur in order
        token_set = ["*", "=", "-", "+"]
        operands = deque([item for item in tokens if item in token_set])
        stack = deque(tokens)

        # map operand to func
        def operand_func(token, a, b):
            if token == "+":
                return a + b
            elif token == "-":
                return a - b
            elif token == "*":
                return a * b
            elif token ==  "/":
                return a // b

        cur_operand = operands.popleft()
        result = 0
        while len(stack) != 1:
            token = stack.popleft()
            if token == "+":
                cur_operand = operands.popleft()
            elif token == "*":
                cur_operand = operands.popleft()
            elif token == "-":
                cur_operand = operands.popleft()
            elif token == "/":
                cur_operand = operands.popleft()
            else:
                result = operand_func(cur_operand, result, int(token))
  
        return result