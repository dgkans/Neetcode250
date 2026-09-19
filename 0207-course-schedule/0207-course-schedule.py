from collections import defaultdict
from typing import List


class Solution:
    def canFinish(
        self,
        numCourses: int,
        prerequisites: List[List[int]]
    ) -> bool:

        # Maps each course to the prerequisites it requires
        prereqs = defaultdict(list)

        for course, prerequisite in prerequisites:
            prereqs[course].append(prerequisite)

        def cycle(course, seen):
            # Reaching a course on the current path means a cycle
            if course in seen:
                return True

            # Mark this course as currently being explored
            seen.add(course)

            # Check each prerequisite for a circular dependency
            for prerequisite in prereqs[course]:
                if cycle(prerequisite, seen):
                    return True

            # All dependencies are safe; skip them in future calls
            prereqs[course] = []

            # Backtrack: this course leaves the current path
            seen.remove(course)

            # No cycle was found through this course
            return False

        # Contains only courses on the active DFS path
        seen = set()

        # Check every course, including disconnected groups
        for course in range(numCourses):
            # A detected cycle means we cannot finish all courses
            if cycle(course, seen):
                return False

        # No cycle exists in any group
        return True