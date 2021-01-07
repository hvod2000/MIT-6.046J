def get_schedule(intervals):
    def binary_search_for_p(i):
        f, n = intervals[i][1], len(intervals) - 1
        while n - i > 1:
            m = (i + n) // 2
            i, n = (i, m) if intervals[m][0] >= f else (m, n)
        return i if intervals[i][0] >= f else n
    intervals = list(sorted(intervals, key=lambda i: i[0])) + [[float('inf')]]
    p = [binary_search_for_p(i) for i in range(len(intervals) - 1)]
    optR = [0 for i in range(len(intervals))]
    take = [None for i in range(len(intervals))]
    for i in range(len(intervals) - 2, -1, -1):
        v_if_leave = optR[i + 1]
        v_if_take = optR[p[i]] + intervals[i][2]
        take[i] = v_if_take > v_if_leave
        optR[i] = v_if_take if take[i] else v_if_leave
    def get_result():
        i = 0
        while i < len(intervals) - 1:
            if take[i]:
                yield intervals[i]
            i = p[i] if take[i] else i + 1
    return list(get_result())
