def get_schedule(intervals):
    result = []
    finish = float("-inf")
    for interval in sorted(intervals, key=lambda i: i[1]):
        if finish <= interval[0]:
            finish = interval[1]
            result.append(interval)
    return result
