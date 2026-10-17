
class Solution:
    def insert(self, intervals: List[List[int]],
               newInterval: List[int]) -> List[List[int]]:

        result = []
        i = 0
        n = len(intervals)

        # 1. Intervals entirely before newInterval
        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1

        # 2. Merge overlapping intervals
        merged = newInterval[:]

        while i < n and intervals[i][0] <= merged[1]:
            merged[0] = min(merged[0], intervals[i][0])
            merged[1] = max(merged[1], intervals[i][1])
            i += 1

        # 3. Append the expanded interval
        result.append(merged)

        # 4. Append all remaining intervals
        while i < n:
            result.append(intervals[i])
            i += 1

        return result
