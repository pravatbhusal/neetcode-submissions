"""
The hard part of this problem is the count() function to figure out the
geometry of the square points.

A square must two points with the same x-axis as the given point.
Ex: count(2, 1) means that there must be another point on x = 2.
Then calculate the distance to that other point to figure out the
distance to use between other points on the cartesian grid.

Store the points in a 2D dict where key = x and value = dict of key = y-value, value = freq count
This lets us find all points on the same x-axis in O(1) time.

We multiply the count of a point's frequency to get the # combinations to
make a square from using only that point.
"""
class CountSquares:

    def __init__(self):
        self.points = defaultdict(lambda: defaultdict(int))

    def add(self, point: List[int]) -> None:
        self.points[point[0]][point[1]] += 1

    def count(self, point: List[int]) -> int:
        x1, y1 = point
        total = 0
        for y2, freq in list(self.points[x1].items()):
            if y1 == y2:
                continue

            # equi-distance for square calculated from (x1, y1) and (x1, y2)
            distance = abs(y1 - y2)

            # point (x1, y2)
            vert_combos = self.points[x1][y2]
            
            # point for square's left-side (x2, y1)
            x2 = x1 - distance
            left_combos = self.points[x2][y1]
            # point for square's left-side (x2, y2)
            left_combos *= self.points[x2][y2]
            
            # point for square's right-side (x2, y1)
            x2 = x1 + distance
            right_combos = self.points[x2][y1]
            # point for square's right-side (x2, y2)
            right_combos *= self.points[x2][y2]

            # sum total square combinations at this x-axis
            total += vert_combos * (left_combos + right_combos)

        return total
