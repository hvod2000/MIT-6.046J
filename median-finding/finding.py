def get_median_of_columns(elements):
    cols = [[] for _ in range((len(elements) + 4) // 5)]
    for i, elem in enumerate(elements):
        cols[i // 5].append(elem)
    medians = [col[(len(col) - 1) // 2] for col in cols]
    if len(medians) == 1:
        return medians[0]
    return get_by_index(medians, (len(medians) - 1) // 2)

def get_by_index(elements, i):
    x = get_median_of_columns(elements)
    elements_before = {e for e in elements if e < x}
    elements_after = {e for e in elements if e > x}
    rank_of_x = len({e for e in elements if e <= x})
    if rank_of_x == i + 1:
        return x
    elif rank_of_x > i:
        return get_by_index(elements_before, i)
    else:
        return get_by_index(elements_after, i - rank_of_x)
