class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) < 2:
            return intervals
        
        intervals = sorted(intervals, key = lambda x : x[0])

        output = [intervals[0]]

        for start, end in intervals:
            last_end = output[-1][1]

            if start <= last_end:
                output[-1][1] = max(end, last_end)
            else:
                output.append([start,end])
        
        return output