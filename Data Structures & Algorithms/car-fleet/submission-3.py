class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # steps = (target - position) / speed
        # merge car fleets that collide before they arrive to target
        # sorting the fleet tells us which car will arrive to the target first
        # new fleet is when there are more steps to take to arrive to target

        # Sort cars by position, closest to target first
        # tuple comparator gives 0th index precedence and uses 1th index as a tie breaker
        pairs = sorted(zip(position, speed), reverse=True)

        fleets = 0
        collide_steps = 0
        for pos, speed in pairs:
            steps = (target - pos) / speed
            if steps > collide_steps:
                # more steps to take, so this is a new fleet
                fleets += 1
                collide_steps = steps
        
        return fleets


    # WRONG: we assumed a car fleet is if they take the exact same number of step
    # A fleet forms when a faster car catches up to a slower car ahead of it, so they may not have same # of steps
    def carFleet_wrong_set_solution(self, target: int, position: List[int], speed: List[int]) -> int:
        # there are 5 cars on a one-way lane
        # example: position[0] is the position of the 1st car, speed[0] is the speed of the 1st car
        # target is the distance to the final destination
        # question is: how many cars will speed together (fleet) until they arrive to target?
        # pos = [1, 4], speed = [3, 2] -> 1 + 3 = 4, 4 + 2 = 6 ; 4 + 3 = 7, 6 + 2 = 8 ; 7 + 3 = 10, 8 + 2 = 10
        
        # steps = (target - position) / speed
        # example: (10 - 4) / 2 = 3 steps - together
        # example: (10 - 1) / 2 = 4.5 steps - separate
        # example: (10 - 0) / 1 = 10 steps - separate
        # example: (10 - 7) / 1 = 3 steps - together

        steps = []
        for i, pos in enumerate(position):
            num_steps = (target - pos) / speed[i]
            steps.append(num_steps)

        # make steps into set to get # of unique steps (fleets)
        return len(set(steps))