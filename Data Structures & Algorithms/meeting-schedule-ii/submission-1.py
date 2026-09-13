'''
Questions: 
    -So the condition where the ending and start time are equal, those two meetings can overlap?
    -Is sorting here allowed or are we looking for an approach that does better than O(nlogn)?
    -Is there a memory complexity threshold?

Solution:
-We would want to start the intervals our by starting time. We can place these intervals in a heap. We then would pop from our heap and see if the earliest end time is <= the current interval's end-time. We can do this by implementing a min-heap where we are sorting our heap by our end time. If they don't overlap we then pop from our heap and push the new interval, if they do overlap then we just push. At the end we just return the length of the heap which would represent the number of meeting rooms that we needed. 



'''

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x: x.start)
        heap = []

        for interval in intervals:
            if heap and heap[0] <= interval.start:
                heapq.heappop(heap)
            heapq.heappush(heap, interval.end)

        return len(heap)

        