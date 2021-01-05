def get_schedule(intervals):
    intervals = list(sorted(intervals, key=lambda i: -i[1]))
    intervals.append((None, float('-inf')))
    p = [-1 for i in range(len(intervals))]
    for i, interval in enumerate(intervals):
        for j in range(i - 1, -1, -1):
            pint = intervals[j]
            if pint[0] > interval[1]:
                p[i] = j
                break
    optR = [0 for i in range(len(intervals))]
    take = [None for i in range(len(intervals))]
    for i in range(len(intervals)):
        v_if_leave = optR[i - 1]
        v_if_take = optR[p[i]]
        if p[i] != -1:
            v_if_take += intervals[p[i]][2]
        take[i] = v_if_take > v_if_leave
        optR[i] = v_if_take if take[i] else v_if_leave
    def get_result():
        tail = len(intervals) - 1
        while tail > 0:
            if take[tail]:
                yield intervals[p[tail]]
            tail = p[tail] if take[tail] else tail - 1
    return list(get_result())
