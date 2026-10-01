from collections import deque


class HitCounter:
    def __init__(self):
        # Store timestamps in arrival order
        self.hits = deque()

    def hit(self, timestamp):
        # Each call records a separate hit
        self.hits.append(timestamp)

    def getHits(self, timestamp):
        # Check the oldest hit while the queue is nonempty
        while len(self.hits) > 0:
            oldest_time = self.hits[0]

            # Remove hits outside the 300-second window
            if timestamp - oldest_time >= 300:
                self.hits.popleft()
            else:
                # All remaining hits are recent enough
                break

        # Outside the loop: only valid hits remain
        return len(self.hits)