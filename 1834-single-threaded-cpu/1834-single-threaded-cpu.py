import heapq
from typing import List

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        pending = []      # tasks not yet arrived: (enqueueTime, processTime, index)
        available = []    # tasks arrived and waiting: (processTime, index)
        
        # Put all tasks in pending heap
        for i in range(len(tasks)):
            enqueueTime = tasks[i][0]
            processTime = tasks[i][1]
            heapq.heappush(pending, (enqueueTime, processTime, i))
        
        time = 0
        res = []
        
        while pending or available:
            # Move all arrived tasks from pending → available
            while pending and pending[0][0] <= time:
                enqueueTime, processTime, i = heapq.heappop(pending)
                heapq.heappush(available, (processTime, i))
            
            # If nothing available, jump time forward
            if not available:
                time = pending[0][0]
                continue
            
            # Run the best available task
            processTime, i = heapq.heappop(available)
            time += processTime
            res.append(i)
        
        return res