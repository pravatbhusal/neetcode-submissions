class MinStack:

    def __init__(self):
        # use python lib Deque, which append() pop() like a Stack
        self.stack = deque()
        # store local min node when inserting a new node
        self.min_stack = deque()

    def push(self, val: int) -> None:
        if len(self.min_stack) > 0:
            local_min = self.min_stack[-1]
        else:
            local_min = sys.maxsize
        self.stack.append(val)
        max_min = val if val < local_min else local_min
        self.min_stack.append(max_min)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        # get head node, check from end of deque (LIFO)
        return self.stack[-1]

    def getMin(self) -> int:
        # idea #1: just keep track of min in a member variable
        # hard part is if we pop, then we need to recheck min O(1) time
        
        # idea 2: can we use a heap to keep track of min?
        # no, popping from heap is O(log(N))

        # BEST: hint from leetcode is each node stores the min at that point of time
        # you can create another python lib Stack to store the min at point of time
        return self.min_stack[-1]
