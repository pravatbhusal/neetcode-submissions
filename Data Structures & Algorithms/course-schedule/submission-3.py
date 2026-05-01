"""
Question says to return an "ordering of courses", which tells me we need Topological Sort.

Topological sort returns the nodes in order of dependencies, which is a perfect solution
for course scheduling. If we detect a cycle, then we cannot finish the courses in order,
return empty array.

Topological sort is "abstract" graph algorithm, a real implementation is Khan's algorithm.
"""
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # fill course pre-requisite dict (adjacency list)
        # pre_req (key) -> courses (set) that are unlocked after taking pre_req
        # in_degree list is the number of pre-reqs that point to course
        courses = defaultdict(list)
        in_degree = [0] * numCourses
        for course, pre_req in prerequisites:
            courses[pre_req].append(course)
            in_degree[course] += 1

        # add all courses that have no pre-reqs
        queue = deque()
        for course in range(numCourses):
            if in_degree[course] == 0:
                queue.append(course)

        result = []
        while queue:
            # take course
            course = queue.popleft()
            result.append(course)

            for next_course in courses[course]:
                # completed this pre-req, decrement
                in_degree[next_course] -= 1
                if in_degree[next_course] == 0:
                    # all pre-reqs complete, course can be taken
                    queue.append(next_course)

        if len(result) == numCourses:
            # all courses complete
            return True
        # all courses could not be completed
        return False

        