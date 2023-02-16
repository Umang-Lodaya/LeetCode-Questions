class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        i = 1
        while i < len(intervals):
            if intervals[i-1][1] >= intervals[i][0]:
                s = min(intervals[i-1][0], intervals[i][0])
                e = max(intervals[i-1][1], intervals[i][1])
                del intervals[i-1]
                intervals[i-1] = [s, e]
                i -= 1
            i += 1
        
        return intervals