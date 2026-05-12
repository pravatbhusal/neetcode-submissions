"""
Plot this out on a cartesian coordinate, x-axis = position, y-axis = speed
If you make the velocity line on the coordinates, cars that intersect before
position = target would be the number of collisions. The number of collisions
are the total car fleets that arrive at position = target.

How can we mimic this cartesian coordinate to find the number of collisions?
On a cartesian coordinate, x and y axes are sorted from [0, ..., infinity]
To mimic this, we also need to sort the (position, speed) in order.

We'll sort in reverse order to compute starting from the cars that are ahead
in the position. Then iterate that and collide cars that are faster than the
previous car and collide before arriving to the target.

This formula is how many steps (time) till car arrives to the target:
steps = (target - position) / speed

If car_2 is behind car_1 (position), but car_1 will arrive to target before car_2 (steps),
then those two cars will collide and become a fleet.

This can be solved using a monotonic increasing stack. Every time you push a new time,
you immediately check if it's <= the element before it. If it is, you pop it.
So any element that would break the increasing order gets removed.
"""
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        
        stack = []
        for pos, speed in cars:
            steps = (target - pos) / speed
            stack.append(steps)
            if len(stack) >= 2:
                car_1 = stack[-1]
                car_2 = stack[-2]
                if car_2 >= car_1:
                    # car_2 will collide with car_1, forms a fleet
                    stack.pop()

        return len(stack)

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