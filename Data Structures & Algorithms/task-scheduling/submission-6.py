class Solution:
    """
    tasks[i] = char from A - Z
    
    1 CPU cycle = do 1 task
    
    n = 2
    if tasks[i] == tasks[j], must be separated by at least 2 cycles
    meaning there must 2 wait states in-between the same task

    Ex: ["X", "X", "Y", "Y"], n = 2
    X -> Y -> idle -> X -> Y

    Task X completed, then next cycle Y (1), then next cycle idle (2), and started again.
    """

    """
    Solution: We need to keep track of when the task last completed.
    If task[last_completed] == n, then we can do that task.

    Max heap where last_completed >= n are at the top of the heap.
    That way we prioritize tasks with the longest last_completed first.

    WRONG APPROACH: To minimize idle time, we actually want to greedily prioritize
    most frequent tasks, not the task with the longest last completed.
    
    Ex: ["A","A","A","B","C"], n = 3
    Answer: A -> B -> C - Idle -> Idle -> Idle -> Idle -> A

    But if we did: B -> C -> A -> Idle -> Idle -> Idle -> A -> Idle ...
    It's clear why not doing A first has more cycles.
    """

    """
    Solution: Max heap where the most frequent task is on the top.
    And have a queue which tells us how long to cooldown till we can
    do that task again. If cooldown == 0, then push task to the heap.

    If len(queue) == 0 and len(heap) == 0, then complete.
    """
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # max heap with frequency count
        freqs = Counter(tasks)
        max_heap = []
        for task, freq in freqs.items():
            max_heap.append((-freq, task)) # negate freq to simulate max heap
        heapq.heapify(max_heap)
        
        # task queue to track available_at (cooldown)
        queue = deque()

        cycles = 0
        while max_heap or queue:
            # add available tasks from queue to max heap
            while queue:
                if queue[0][2] > cycles:
                    # no more tasks available, so break
                    break
                task, freq, _ = queue.popleft()
                heapq.heappush(max_heap, (-freq, task))

            if max_heap:
                # get the most frequently occurring task
                freq, task = heapq.heappop(max_heap)

                # do task
                freq *= -1
                freq -= 1
                cycles += 1

                if freq > 0:
                    # all of this task not complete, add back to queue
                    available_at = cycles + n
                    queue.append((task, freq, available_at))
            else:
                # idle — jump to next available task
                cycles = queue[0][2]

        return cycles
        