
from collections import deque
from typing import List

class Solution:
    def canFinish(
        self,
        numCourses: int,
        prerequisites: List[List[int]]
    ) -> bool:

        numC = numCourses
        pre = prerequisites

        # Build the graph
        a = {i: [] for i in range(numC)}
        indeg = [0] * numC

        for course, req in pre:
            a[req].append(course)
            indeg[course] += 1

        # Start with all courses having
        # zero prerequisites
        queue = deque(
            i for i in range(numC)
            if indeg[i] == 0
        )

        done = 0

        while queue:
            node = queue.popleft()
            done += 1

            for neighbor in a[node]:
                indeg[neighbor] -= 1

                if indeg[neighbor] == 0:
                    queue.append(neighbor)

        return done == numC
