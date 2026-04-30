"""
The point of this question is detecting a "cycle" within the graph.
If we detect a cycle, then it's impossible for that course path.

We can make an adjaceny list: Keep a dict of the course (key) with a value
which is the set of the pre-requisite courses.

Then for each course, run DFS to see if it's possible to satisfy numCourses.
To detect cycle, have a set that stores which nodes we've visited in DFS.
"""
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # fill course pre-requisite dict
        courses = defaultdict(list)
        for pair in prerequisites:
            courses[pair[0]].append(pair[1])
        
        # run DFS to see if we can finish the course path
        visited = set()
        path = set()
        def dfs(course):
            if course in path:
                # detected cycle, cannot complete
                return False
            if course in visited:
                # visited this course before, and is safe
                return True
            if courses[course] == []:
                # can complete pre-reqs for this path
                return True
            
            # search the next path of pre-reqs
            path.add(course)
            for crs in courses[course]:
                complete = dfs(crs)
                if not complete:
                    return False
            path.remove(course)

            # add to visited to not traverse this path again
            visited.add(course)
            return True

        # check to finish all courses
        for crs in range(numCourses):
            complete = dfs(crs)
            if not complete:
                return False
        return True
            
