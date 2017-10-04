# Andy Yu
'''
Given a collection of intervals, merge all overlapping intervals.

For example,
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18].

Note:
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

--------------------------------------------------------------------------------

Difficulty: Easy

Solution notes:


O(n) time
O(n) space
'''

def merge(intervals):
    intervals.sort(key=lambda x: x.start)
    results = []
    start = None
    end = None
    for interval in intervals:
        if start is None or end is None:
            start = interval.start
            end = interval.end
            continue
        if interval.start <= end and interval.end >= end:
            end = interval.end
        elif interval.start > end:
            results.append([start, end])
            start = interval.start
            end = interval.end
    if start is not None and end is not None:
        results.append([start, end])
    return results

if __name__ == "__main__":
    print(merge([[2,6],[8,10],[15,18],[1,3]]))
