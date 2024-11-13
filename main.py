def merge_intervals(intervals):
    def sort_key(interval):
        return interval[0]
    intervals.sort(key=sort_key)
    merged = []
    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])
    return merged
intervals = [[1, 3], [2, 4], [6, 8]]
print(merge_intervals(intervals))

