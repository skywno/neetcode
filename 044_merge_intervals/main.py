from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda interval: interval[0])
        res = []
        previous = None
        for current in intervals:
            if previous is None:
                previous = current
            else:
                # check if previous overlaps with the current
                if previous[1] >= current[0]:
                    if previous[1] >= current[1]:
                        previous = [previous[0], previous[1]]
                    else:
                        previous = [previous[0], current[1]]
                else:
                    res.append(previous)
                    previous = current
        if previous is not None:
            res.append(previous)
        return res

    def merge2(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i: i[0])
        output = [intervals[0]]
        for start, end in intervals[1:]:
            lastEnd = output[-1][1]
            if start <= lastEnd:
                output[-1][1] = max(lastEnd, end)
            else:
                output.append([start, end])
        return output